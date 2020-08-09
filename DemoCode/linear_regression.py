def linear_regression(X: list, Y: list) -> list:
    """
    Perform Linear Regression Analysis.

    Args:
        list: input multidimensional list containing
              simulated stock data
        list: input list containing simulated option
              price data

    Returns:
        list: a list containing model parameters
    """
    # Create linear regression object.
    lr_model = linear_model.LinearRegression()

    x = np.array(X)
    y = np.array(Y)

    # Training for call options.
    lr_model.fit(x, y)

    intercept = lr_model.intercept_
    coefficients = lr_model.coef_
    C0 = (lr_model.intercept_
            * np.exp(- 0.026 * T)
            + np.dot(lr_model.coef_, spot_df.values))[0]

    return [intercept, coefficients, C0]
