## Model
A set of rules that describe how data are generated.

## Consistency
Evaluation of the plausibility that data generated from a particular model. In other words, when evaluating a hypothetical scenario, we may ask "Is this outcome consistent with the proposed model?"

## Hypothesis
In statistics, a hypothesis is defined as a null or alternative view of how data were generated from a model.

## Null Hypothesis
The default view that is generally believed to be true.

## Alternative Hypothesis
A hypothesis that is opposite of the null hypothesis.

## Test statistic
A summary measure of the data that we use to investigate the consistency of a model. The choice of a test statistic depends on the specific hypotheses we are investigating. For example, the difference in means, medians, or standard deviations could all be used as test statistics.

## P-value
The chance, under the null hypothesis, that the test statistic is equal to the observed value or is further in the direction of the alernative hypothesis.

## Two Sample Test
A hypothesis test performed to investigate whether there is a difference between two random samples or groups. This is also called A/B testing as we can refer to our two groups as Group A and Group B.

## A/B Test
A hypothesis test performed to investigate whether there is a difference between two random samples or groups (e.g., Group A and Group B). This is also called a Two Sample Test.

## Boxplot
Also called a box and whisker plot, a boxplot is a graphical visualization of a data distribution. The bottom edge of the box demarcates the 25th percentile (Quartile 1, or Q1) of the data. The top edge of the box demarcates the 75th percentile (Quartile 3, or Q3). Thus, the box itself represents the range in which the middle 50% of the data falls (Q3-Q1). This range is also commonly referred to as the Interquartile Range (IQR).

The horizontal line within the box indicates the median value of the distribution (50th percentile). When using the `matplotlib.boxplot()` function, the top whisker (what looks like a T above the box) extends to the largest data point of the distribution that falls within the range $Q3 + 1.5*IQR$. The bottom whisker (what looks like an upside down T below the box) extends to the smallest data point within the range $Q1 - 1.5*IQR$. Data points with a value larger or lower than the whiskers are considered outliers and represented as circles above or below the whiskers.

### Interquartile Range (IQR)
The range in which 50% of datapoints from a distribution fall, also calculated as Quartile 3 (75th percentile) - Quartile 1 (25th percentile).

## Permutation Test
A procedure to shuffle data to approximate the sampling distribution of a test statistic.

## Total Variation Distance (TVD)
Sum of absolute differences in proportions.

$${\rm TVD}=\frac{1}{2} \sum |p_i-q_i|$$

In the above formula, $p_i$'s are proportions of subjects in various categories in one sample while $q_i$'s are proportions in the second sample.

## Significance Level
A cut-off value, $\alpha$, that is used as a threshold to determine whether to accept the null or alternative hypothesis. A commonly used significance level is $\alpha=0.05$. If the p-value is smaller than $\alpha < 0.5$, we reject $H_0$, otherwise we fail to reject it.

## Type 1 error
Rejection of the null hypothesis $H_0$ when it is true. The type 1 error rate is equal to the significance level ($\alpha$). 

## Type 2 error
Failure to reject the null hypothesis $H_0$ when it is false.