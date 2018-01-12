# Function to check dataset for 'speeders' and 'cheaters'

check_data <- function(df,exclude_col=c(1),tol=.5) {
    #' Returns the rows in a dataset for low variance observations
    #'
    #' INPUT
    #'     df (dataframe) the dataset to check
    #'     exclude_col (c() array) the columns to exclude, default is c(1)
    #'     tol (float) return the row if the variance is less than tol, default=.5
    #' RETURNS
    #'     (dataframe) of the rows with variance less than tol
    #'
    out <- c()
    D <- data.matrix(df[,-exclude_col]) # convert to matrix type
    row_var <- apply(D,1,var) # apply the variance function to D row-wise
    return(df[(row_var <= tol),])
}

# Example
check_data_test <- function() {
    df <- read.csv(file = "CS_MD_surveyData.csv", header = TRUE, sep = ",")
    check_data(df,exclude_col=c(1,2))
}

check_data_test()
