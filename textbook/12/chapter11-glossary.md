## Deterministic Sampling
A type of sampling with no random chance involved.

## Probabilistic Sampling
A type of sampling where the probability of each unit being chosen is known before sampling is done. For example, **Sample random samples (SRS)**, in which each unit has equal probability of being chosen, is an example of a probabilistic sample.

## Distributions
Possible outcomes for a random event and their probabilities.

## Probability Distributions
The theoretical likelihood of a distribution. Probability distributions can be studied and understood without collecting any sample or conducting an experiment. See Probability Mass Function and Probability Density Function for examples.

## Empirical probability distributions
The observed distribution that may come from multiple samples or repeated experiments.

## Random variable
A numerical quantity representing an outcome of the event, often denoted by uppercase letters $X$ or $Y$.

## Discrete
Finite or countable infinite elements in its sample space.

## Continuous
Infinite elements in its sample space.

## Discerete Random Variable
Refers occasions where the sample space is a set of possible outcomes. For example, $\{\text{Heads}, \text{Tails} \}$ for the outcome of a coin flip.

## Continuous Random Variable
The sample space is often an interval of possible outcomes. An example of this would be an interval of possible adult heights in inches [24, 107].

## Probability Mass Function (PMF)
A function that assigns the probability of each possible outcome of a random variable for discrete random variables. 

The PMF is usually denoted $P(X=x)$ where $X$ is a random variable and $x$ is the outcome of an event. 

All probabilities, $P(X=x)$, must satisfy the following criteria:
- the probability of each element occurring is greater than or equal to 0
- the sum of all probabilities of elements in the sample space equals 1

## Probability Density Function (pdf) 
A function to compute probabilities for continuous random variables. Unlike the discrete case, where all probabilities in a sample space will sum to 1, in the continuous case this corresponds to an area of 1 under the curve of the probability density function. 

## Expected Value
A common measure of the center of a random variable, defined by $\mu(X)$ or $E(X)$. This describes the average value of the sample space. 

## Variance
The spread of data, symbolized by $\sigma^2(X)=Var(X)$. This describes how the data is dispersed.

## Standard Deviation
The square root of the variance symbolized by $\sigma(X)$. The standard deviation is a measure of how far each element is from the mean, in fact we can think of it as an average measure of how far all our data is from the mean. 

## Sample Mean
Measure of center for an empirical distribution.  Defined as: 
>$\bar{x} = \frac{\Sigma x_i}{n}$ 

## Sample Variance
Measurement of the spread for an empirical distribution. Defined as: 
>$s^2 = \frac{\Sigma (x_i - \bar{x})^2}{n-1}$

### Sample Standard Deviation
The square root of the sample variance, denoted by $s$

## Uniform Distribution
A distribution where all events in a given sample space are equally likely to occur. Examples include, the distribution of possible outcomes when tossing a fair coin, rolling a die, or using a random number generator. Notice these examples include both discrete and continuous random variables.

## Law of Large Numbers
As the number of experiments increases, the mean of the empirical distribution gets closer to the mean of the probability distribution (also known as the expected value).

## Discrete Uniform Distribution
A probability distribution that assigns equal (uniform) probability to all outcomes in a discrete sample space. For example, rolling a fair six-sided die is a discrete uniform distribution, as the theoretical probability of rolling each side is $\frac{1}{6}$

For a sample space containing $n$ elements, the Probability Mass Function (PMF) is defined by:

> $P(X=x)=\frac{1}{n}$ for all x in the sample space S (0 otherwise).

Further, if $E$ is an event containing multiple elements from the sample space, then:

> $P(E)=\frac{\text{Number of elements in E}}{n}$

## Continuous Uniform Distribution
A probability distribution that assigns equal (uniform) probability to each continuous random variable $X$, on the interval $[a, b]$. 

For example, if to randomly sample a random variable from a continuous sample space between 1 and 6, our random variable that takes values between 1 and 6 would be denoted by $X \sim U(1,6)$. 

The PDF for a continuous uniform random variable is:

> $f(x) = \frac{1}{b-a}$ when $x$ is between $a$ and $b$ and 0 otherwise.

From this distribution, we calculate the middle of the interval:

> $\mu = \frac{b+a}{2}$

and the variance:

> $\sigma^2 = \frac{(b-a)^2}{12}$ 

## Normal Distribution
A continuous distribution that is symmetric and bell-shaped. Due to its symmetry, the three measures of center mode, median, and mean, are exactly the same for the normal distribution. Moreover, the normal distribution is defined entirely in terms of its mean and standard deviation. Notationally, given a random variable $X$ that is normally distributed, we can say $X \sim N(\mu,\sigma)$, where $\mu$ and $\sigma$ are the mean and standard deviation of the distribution, respectively.

## Standard Normal Distribution
A special case of the normal distribution that occurs when $\mu = 0$ and $\sigma = 1$. Given a random variable and any values for $\mu$ and $\sigma$, that is $X  ∼  N(\mu, \sigma)$, we can *transform* to a standard normal, by normalizing it! That is:

$$\frac{X-\mu}{\sigma}$$

Note this may be useful if you are comparing values from multiple normal distributions.

## Central Limit Theorem (CLT)
An important mathematical theorem which states that the distribution of sample means from a sufficiently large random sample (with replacement) will be approximately normally distributed. The CTL allows us to estimate the mean and standard deviation of a distribution of sample means. If the mean and standard deviation of the population you are sampling from are $\mu$ and $\sigma$ respectively, then the mean and standard deviation of the distribution of sample means are $\mu$ and $\frac{σ}{\sqrt{n}}$, respectively, where n is the sample size. 

## Binomial Distribution

## Bernoulli Trial

## Normal Approximation to the Binomial Distribution