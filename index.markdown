---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: ""
---

<!-- Table showing predictions --> 

<head>
    <link rel="stylesheet" href="assets\css\table.css">
    <script src="assets\js\table.js"></script>
</head>
<div class="tab">
    <button class="tablinks" onclick="openCity(event, 'Machine Learning')">Machine Learning</button>
    <button class="tablinks" onclick="openCity(event, 'Team Jersey Color')">Team Jersey Color</button>
    <button class="tablinks" onclick="openCity(event, 'Crowd Choice')">Crowd Choice</button>
</div>

<div id="Machine Learning" class="tabcontent">
    
</div>
<div id="Team Jersey Color" class="tabcontent">
    
</div>
<div id="Crowd Choice" class="tabcontent">
    
</div>

## Motivation and Background 
<details markdown="1">
<summary style="display:list-item"><span>Russian Literature & French Statistics</span></summary>

<figure>
  <img src="images\anton-chekhov-new.jpg" id="small-image"> 
    <figcaption>The face of a man that paid for medical school by writing <a href="https://en.wikipedia.org/wiki/Anton_Chekhov#Early_writings">short stories</a>.</figcaption>
</figure>

In Anton Chekhov's 1894 story, ["The Student"](https://americanliterature.com/author/anton-chekhov/short-story/the-student), Ivan is heading home
during a cold March evening. He just left from an encounter with Vasilisa, who cried bitterly when he related to her the Biblical story about [Peter's betrayal](https://en.wikipedia.org/wiki/Denial_of_Peter) that was described as occuring 2,000 years ago.
  
He realizes that it wasn't the way he told the story that moved her, but rather the guilt that Peter himself felt that brought this emotion from Vasilisa.

Ivan then says to himself, 
  
> " 'the past [...] is linked with the present by an unbroken chain of events flowing one out of another' "


<figure>
  <img src="images\9uekyze10wd41.jpg" id="small-image"> 
    <figcaption></figcaption>
</figure>


> "[...] it seemed to him that he had just seen both ends of that chain; that when he touched one end the other quivered."


This chain of causality that Chekhov described was not a new idea in the late 19th century. Earlier in 1814, the French polymath, Pierre-Simon Laplace, wrote in his book [A Philosophical Essay on Probabilities](https://bayes.wustl.edu/Manual/laplace_A_philosophical_essay_on_probabilities.pdf)


> "Present events are connected with preceding ones by a tie based upon the evident principle that a thing cannot occur without a cause which produces it." 


He then proposed a thought: if a sufficiently intelligent being knew the present state of every single granularity of the Universe, that is, every causal link, then this being would be able to perfectly predict the future as well as retrace the past.


> "[...] an intelligence which could comprehend all the forces by which nature is animated and the respective situation of the beings who could compose it - an intelligence sufficiently vast to submit these data to analysis [...] for it; nothing would be uncertain and the future, as the past, would be present to its eyes" 


As if an approximation to this hypothetical intelligence, the field of computational statistical learning emerged as a way to predict outcome using historical data. Writing about the positive examples of these algorithms would further indulge a field already saturated with promises of the future. 


<figure>
  <img src="images\man.jpg" id="med-image"> 
    <figcaption>"Since you are pressing the pedal, I predict a 97% chance that you want the car to move forward."</figcaption>
</figure>


And this field doesn't seem to gate-keep either. 

With publicly available packages such as [sklearn](https://scikit-learn.org/stable/), [keras](https://keras.io/), and [tensorflow](https://www.tensorflow.org/) the bar to start using machine learning has never been lower.

In conjunction with the availability of [open-source datasets](https://www.kaggle.com/datasets), it seems that every field is now open to modeling to even the most amateur of programmers. 

This field promises: not everyone can be an expert, but with the right tools and resources, they can create models that perform like experts. 
</details>

<details markdown="1">
<summary style="display:list-item"><span>American Basketball</span></summary> 

But can we really explore a field for which we have no "domain knowledge" of and create predictions that suprass the foresight of experts? 

This question is especially relevant when we deal with human-centered fields.

For example, within the neary 100-year history of the NCAA's college basketball tournemant "March Madness", a 16-seeded team has never won against a 1-seeded team. That is, until 2018. 

<figure>
  <img src="images\header-1.jpg" id="large-image">  
    <figcaption>UMBC v. Virginia</figcaption>
</figure>

Could an algorithm have predicted this performance, even though no basketball "expert" had the abiltiy to predict such an outcome? 

In 2018 I trained a classifier on team-ranking data from basketball enthusiasts. It gave UMBC a 2% chance of victory. Perhaps a model with "better" data would have even given it a 0% chance.

This year, my methodology hasn't changed. Instead, I take a step back and realistically ask: "do I even bother modelling a field for which I have no knowledge on?"

As someone who has never watched a basketball game out of enjoyment, my knowledge of basketball terminology limited to "triple-double" because of Ice-Cube's "It Was a Good Day."

So, I compare my models results to the following "non-data driven" bracket predictions:

- the winner always has the more popular [team color](https://www.spoonflower.com/americas_true_colors). 
- the winner is chosen by the [wisdom of crowds](https://fantasy.espn.com/tournament-challenge-bracket/2021/en/nationalBracket)

Through this comparison, I begin asking: 

- Is it just as bad to guess (or forgo data when making predictions) than create a model for a poorly-understood field? 
- Does all data point to an interesting & predictive model.
- Are there fields where algorithms will never be as good as the opinion of "experts"
- Do experts even exist when it comes to "prediction"?
</details>

## The Data
<details markdown="1">
<summary style="display:list-item"><span>Expert Systems</span></summary>

<figure>
  <img src="images\massey-sample.png" id="med-image">  
    <figcaption>Subset of "Massey Ordinals" pulled from <a href="https://www.kaggle.com/c/ncaam-march-mania-2021/data">Kaggle</a></figcaption>
</figure>

I relied on ordinal data generated by basketball enthusiasts in a data-set called <a href="https://www.masseyratings.com/cb/compare.htm">Massey Ordinals</a>. The ordinal ranking data placed college basketball teams on a ranked scale based on human-interpreted past performance.

So, the "best" team would have a rank of #1 while the "worst" team will be ranked at the last position (if there are 353 basketball teams competing, it would be ranked as #353). 

Through some 

<br><br>
</details >

## Conclusions
<details markdown="1">
<summary style="display:list-item"><span>Observations on Predicted Bracket</span></summary>

My model contains no interesting upset predictions. In fact, I don't think anyone would particularly enjoy a tournemant that falls in-line with my model. 

The fun of "March Madness" is seeing underdogs such as 2018 Loyola accomplish that which all the "experts" deem as unlikely: beat lower-seeded teams. And not just accomplish that once, but enough times to reach the Final Four.

<img src="images\fans.jpg" id="large-image"> 

In fact, life's most exciting moments are arguably when the unlikely becomes realized. For example, retail investors making millions off of the stock market.


<img src="images\stonk.jpg" id="small-image"/>

<br><br>
</details >

<details markdown="1">
<summary style="display:list-item"><span>Motivation for further development</span></summary>

- How many of these problems can be mollified by "good" statistics?
  - Ex: finding significant attributes, boot-strapping models, determining causality
- How many of these problems can be mollified by "good" data-collection?
  - Ex: Data on stadium location, rate of injury
- Would a model that only looks for "upsets" be as good as a "chalk" model? 
<br><br>
</details >

## Meme tax 

<img src="images\4c7r0e.jpg" id="small-image"/>