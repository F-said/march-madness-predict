---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: ""
---
## Motivation and Background 
<details markdown="1">
<summary style="display:list-item"><span>Russian Literature, French Statistics, & American Basketball</span></summary>

<figure>
  <img src="images\anton-chekhov-new.jpg" id="headshot"> 
    <figcaption>The face of a man that paid for medical school by writing short stories on the weekend</figcaption>
</figure>

In Anton Chekhov's 1894 short story, ["The Student"](https://americanliterature.com/author/anton-chekhov/short-story/the-student), Ivan Velikopolsky is heading home
during a cold March evening. He just left from an encounter with a friend, Vasilisa, who cried bitterly when he told her the Biblical story about [Peter's betrayal](https://en.wikipedia.org/wiki/Denial_of_Peter) that was described as occuring 2,000 years ago.
  
He realizes that it wasn't the way he told the story that moved her, but rather the guilt that Peter himself felt that brought this emotion from Vasilisa.

Ivan then says to himself, 
  
> " 'the past[...] is linked with the present by an unbroken chain of events flowing one out of another' "

> "[...] it seemed to him that he had just seen both ends of that chain; that when he touched one end the other quivered."

This chain of causality that Chekhov described might have been inspired by the French polymath, Pierre-Simon Laplace, who in 1814 wrote in his book [A Philosophical Essay on Probabilities](https://bayes.wustl.edu/Manual/laplace_A_philosophical_essay_on_probabilities.pdf)

> "Present events are connected with preceding ones by a tie based upon the evident principle that a thing cannot occur without a cause which produces it." 

<figure>
  <img src="images\9uekyze10wd41.jpg" id="headshot"> 
    <figcaption></figcaption>
</figure>

He then proposed a thought experiment: if a sufficiently intelligent being knew the present state of every single granularity of the Universe, that is, every causal link, then this being would be able to perfectly predict the future as well as retrace the past.

> "[...] an intelligence which could comprehend all the forces by which nature is animated and the respective situation of the beings who could compose it - an intelligence sufficiently vast to submit these data to analysis ... for it; nothing would be uncertain and the future, as the past, would be present to its eyes" 

It is only appropriate that the field of computational statistical learning emerged as a way to predict outcome using historical data. 

But are the methods of prediction within this field sufficient when we start to introduce unpredictable humans?

For example, within the neary 100-year history of the NCAA's college basketball tournemant "March Madness", a 16-seeded team has never won against a 1-seeded team. That is, until 2018 when the 16-seeded UMBC upset the 1-seeded Virginia. 

<img src="images\header-1.jpg" id="basketballpan"> 


Could an algorithm have predicted this performance? 

In 2018 I trained a classifier on college basketabll team-ranking data. It gave UMBC a 2% chance of victory for that game against. Perhaps a "better" model would have even given it a 0% chance of victory.

This year, my methodology hasn't changed, so I expect my model to miss major upsets. Instead I propose to compare my models results to a bracket that I generated using "unpredictive" principles. Namely, predicting that the winner always has the more popular team color (everyone loves blue!).

Through this approach, I hope to ask the following question: is it better to sometimes guess than use potentially biased data/improperly trained model? 
</details>

## Results 
<!-- Table showing predictions --> 

<head>
    <link rel="stylesheet" href="assets\css\table.css">
    <script src="assets\js\table.js"></script>
</head>
<div class="tab">
    <button class="tablinks" onclick="openCity(event, 'Machine Learning')">Machine Learning</button>
    <button class="tablinks" onclick="openCity(event, 'Color')">Color</button>
</div>
<div id="Machine Learning" class="tabcontent">
    <p> Insert Image Here</p>
</div>
<div id="Color" class="tabcontent">
    <p> Insert Image Here</p>
</div>
<br>

## The Algorithm(s)
<details markdown="1">
<summary style="display:list-item"><span>90% data, 10% science</span></summary>
<br>
</details >

## The Data(s)
<details markdown="1">
<summary style="display:list-item"><span>Expert Systems</span></summary>
<br>
</details >


## Conclusions
<details markdown="1">
<summary style="display:list-item"><span>Observations on Predicted Bracket</span></summary>

My model contains no interesting upset predictions. In fact, I don't think anyone would particularly enjoy a tournemant that falls in-line with my model. 

The fun of "March Madness" is seeing underdogs such as 2018 Loyola accomplish that which all the "experts" deem as unlikely: beat lower-seeded teams. And not just accomplish that once, but enougth times to reach the Final Four.

<img src="images\fans.jpg" id="basketballpan"> 

In fact, life's most exciting moments are arguably when the unlikely becomes realized. For example, retail investors making millions off of the stock market.

<img src="images\stonk.jpg" id="headshot"/>

Training a model on expert data will introduce bias into a model if all the experts fall in line. This will obviously make it "blind" to those unexpected moments we enjoy.

But it still has its validity. As someone that has never watched a basketball game out of enjoyment, I have no domain knowledge on this sport. In result I have two paths to take: I can either rely on the establishment's collective knowledge and the data-based that they create metrics; or I can take the path of self-education and attempt to create metrics myself.

The latter obviously seems like the riskier option. 
<br>
</details >

<details markdown="1">
<summary style="display:list-item"><span>Motivation for further development</span></summary>

- Some ordinal rankings were unavailable this year. This made my training set contain high bias. Can I create a model that generates ordinal rank?
<br>
</details >

<details markdown="1">
<summary style="display:list-item"><span>Looking Forward</span></summary>

This year, the model I initially created was trained on data that was no longer available. Can I create a model
<br>
</details >

<details markdown="1">
<summary style="display:list-item"><span>Resources</span></summary>


<br>
</details >

## Meme tax 

<img src="images\4c7r0e.jpg" id="headshot"/>