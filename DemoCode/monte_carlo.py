# Accelerate computation using Numba @njit option and
# activate parallel computing.
@njit(parallel=True, fastmath=True)
def simulation(num_simulations: int, st: np.array(), ct: np.array(), pt: np.array(), st_ind: np.array()):
    """
    Compute Monte Carlo simulation to generate stock paths
    for basket option pricing. Here we are computing both
    the call option and the put option.

    Args:
        int: number of simulations num_simulations
        np.array(): numpy array st to store simulated stock
                    prices
        np.array(): numpy array ct to store simulated call
                    option prices
        np.array(): numpy array pt to store simulated put
                    option prices
        np.array(): two dimensional numpy array to store
                    simulated stock price paths for each
                    individual stock

    Returns:
        None
    """
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

