---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: ""
---
## Motivation and Background 

In Anton Chekhov's 1894 short story, ["The Student"](https://americanliterature.com/author/anton-chekhov/short-story/the-student), Ivan Velikopolsky is heading home
during a cold March evening. He just left from an encounter with a friend, Vasilisa, who cried bitterly when he told her the Biblical story about [Peter's betrayal](https://en.wikipedia.org/wiki/Denial_of_Peter) that was described as occuring 1,900 years ago.
  
And in that moment, he realized that it wasn't the way he told the story that moved her, but rather the guilt that Peter himself felt that brought this emotion from Vasilisa.

Ivan then says to himself, 
  
> the past... is linked with the present by an unbroken chain of events flowing one out of another

> ... it seemed to him that he had just seen both ends of that chain; that when he touched one end the other quivered.

This chain of causality that Chekhov described might have been inspired by the French father of statistics, Pierre Simon de-Laplace, who in 1814 wrote, 

> Present events are connected with preceding ones by a tie based upon the evident principle that a thing cannot occur without a cause which produces it. (A Philosophical Essay on Probabilities Ch 2, Pg 3)

He then proposed a thought experiment: if a sufficiently intelligent being knew the present state of every single granularity of the Univerise, that is every causal link, then this being would be able to perfectly predict the future as well as retrace the past.

> ... an intelligence which could comprehend all the forces by which nature is animated and the respective situation of the beings who could compose it - an intelligence sufficiently vast to submit these data to analysis ... for it; nothing would be uncertain and the future, as the past, would be present to its eyes (A Philosophical Essay on Probabilities Ch 2, Pg 4)

It is  only appropriate then that field of computational statistical learning emerged as a way to predict outcome on historical data. 

But is this a sufficient mode of prediction when we start to introduce the most unpredictable element of the universe, humans?

Specifically, humans playing basketball.

I present my March Madness algorithm that generates probabilities from historical ranking data. The methodology and data used is explained below. 

And just to see how wrong my algorithm is, I compare my bracket to a number of other brackets that use the following methods to predict the outcome of a college basketball: 

- Winner is predicted to always have have stronger mascot (bull vs. wasp)
- Winner is predicted to always have the more popular team color (everyone loves blue!)
- Winner is predicted to always be the collectively tallest team (less distance to rim)

## Results 
<!-- Table showing predictions --> 
<html> 
    <head>
        <link rel="stylesheet" href="assets\css\table.css">
        <script src="assets\js\table.js"></script>
    </head>
    <div class="tab">
        <button class="tablinks" onclick="openCity(event, 'Machine Learning')">Machine Learning</button>
        <button class="tablinks" onclick="openCity(event, 'Mascot')">Mascot</button>
        <button class="tablinks" onclick="openCity(event, 'Color')">Tokyo</button>
        <button class="tablinks" onclick="openCity(event, 'Height')">Tokyo</button>
    </div>
    <div id="Machine Learning" class="tabcontent">
        <h3>London</h3>
            <p>London is the capital city of England.</p>
    </div>
    <div id="Mascot" class="tabcontent">
        <h3>Paris</h3>
        <p>Paris is the capital of France.</p>
    </div>
    <div id="Color" class="tabcontent">
        <h3>Tokyo</h3>
            <p>Tokyo is the capital of Japan.</p>
    </div>
    <div id="Height" class="tabcontent">
        <h3>Tokyo</h3>
            <p>Tokyo is the capital of Japan.</p>
    </div>
</html>

## The Algorithm

## The Data

## Further Questions
- Does everything have a predictive model?
- Is all data predictive?
- Is it better to sometimes guess than use a sophisticated (but wrong) model. 
- Can simple data be effectively used? 

## Meme tax 

<img src="images\4c7r0e.jpg" width="300" height="400" class="center"/>