is_narcissistic <- function(num) {
  digits <- as.numeric(unlist(strsplit(as.character(num), "")))
  num_digits <- length(digits)
  sum_of_powers <- sum(digits^num_digits)
  return(sum_of_powers == num)
}
