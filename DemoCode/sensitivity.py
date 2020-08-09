call_strike = 40
num_simulations = 10**6

call_strikes = np.zeros(20)
C0_call_strike = np.zeros(20)

@njit(parallel=True, fastmath=True)
def simulation_strike(num_simulations, st, ct, pt, st_ind, strike):
        for i in prange(num_simulations):

            # Compute current spot stock price.
            stock_prices = spot_prices * np.exp((0.026 - 0.5 * sigmas ** 2) * T + cor_random_nums[i] * sigmas * np.sqrt(T))
            st_ind[i,:] = stock_prices
            st_basket = np.dot(stock_prices, W)
            st[i] = st_basket

            # Compute call price.
            ct[i] = max(st_basket - strike, 0)

            # Compute put price.
            pt[i] = max(strike - st_basket, 0)

for i in range(20):
    st = np.zeros(num_simulations) # stock prices
    ct = np.zeros(num_simulations) # call prices
    pt = np.zeros(num_simulations) # put prices
    st_ind = np.zeros((num_simulations, num_stocks)) # individual stock prices

    simulation_strike(num_simulations, st, ct, pt, st_ind, call_strike)

    # Create linear regression object.
    lr_model = linear_model.LinearRegression()

    x = np.array(st_ind)
    y = np.array(ct)

    # Training for call options.
    lr_model.fit(x, y)
    C0_linear_model = (lr_model.intercept_ * np.exp(- 0.026 * T) + np.dot(lr_model.coef_, spot_df.values))[0]

    C0_call_strike[i] = C0_linear_model
    call_strikes[i] = call_strike

    call_strike += 2
