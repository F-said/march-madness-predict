
R version 3.4.2 (2017-09-28) -- "Short Summer"
Copyright (C) 2017 The R Foundation for Statistical Computing
Platform: x86_64-apple-darwin15.6.0 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

[R.app GUI 1.70 (7434) x86_64-apple-darwin15.6.0]

[History restored from /Users/farukhsaidmuratov/.Rapp.history]

> // Cool lib provided by Zach Mayer https://github.com/zachmayer/kaggleNCAA
> library('kaggleNCAA')
> dat <- parseBracket('/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/submission2018gb.csv', w=0)
> sim <- simTourney(dat, 1000, progress=TRUE)
> bracket <- extractBracket(sim)
> printableBracket(bracket) 
assuming women = 0
> 
