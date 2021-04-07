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
    <link rel="stylesheet" href="assets\css\tourney.css">
</head>

<div class="tab">
    <button id="ML" class="tablinks" onclick="switchBracket(event, 'Machine Learning')">Machine Learning</button>
    <button id="TC" class="tablinks" onclick="switchBracket(event, 'Team Jersey Color')">Team Jersey Color (Guessing)</button>
    <button id="CC" class="tablinks" onclick="switchBracket(event, 'Crowd Choice')">Crowd Choice</button>
</div>

<div id="Machine Learning" class="tabcontent">
  <section id="bracket">
    <div class="round-details">33/62 Correctly Predicted</div>
	  <div class="container">
	    <div class="split split-one">
		    <div class="round round-one current">
			    <div class="round-details">First Round</div>
			      <ul class="matchup">
				      <li class="team team-top">Gonzaga</li>
				      <li class="team team-bottom lost">Norfolk State</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">Oklahoma</li>
				      <li class="team team-bottom">Missouri</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Creighton</li>
				      <li class="team team-bottom">UCSB</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Virginia</li>
				      <li class="team team-bottom">Ohio</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">USC</li>
				      <li class="team team-bottom">Drake</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Kansas</li>
				      <li class="team team-bottom">Eastern Washington</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Oregon</li>
				      <li class="team team-bottom">VCU</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Iowa</li>
				      <li class="team team-bottom">Grand Canyon</li>
			      </ul>
            <ul class="matchup">
				      <li class="team team-top">Michigan</li>
				      <li class="team team-bottom">Texas Southern</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">LSU</li>
				      <li class="team team-bottom">St. Bonaventure</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Colorado</li>
				      <li class="team team-bottom">Georgetown</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Florida State</li>
				      <li class="team team-bottom">UNC Greensboro</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">BYU</li>
				      <li class="team team-bottom">UCLA</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Texas</li>
				      <li class="team team-bottom">Abilene Christian</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">UConn</li>
				      <li class="team team-bottom">Maryland</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Alabama</li>
				      <li class="team team-bottom">Iona</li>
			      </ul>											
		      </div>	<!-- END ROUND ONE -->
          <div class="round round-two current">
            <div class="round-details">Second Round</div>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Gonzaga</li>
              <li class="team team-bottom" id="correct">Oklahoma</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Creighton</li>
              <li class="team team-bottom" id="wrong">Virginia</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">USC</li>
              <li class="team team-bottom" id="correct">Kansas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="correct">Oregon</li>
              <li class="team team-bottom" id="correct">Iowa</li>
            </ul>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Michigan</li>
              <li class="team team-bottom" id="wrong">St. Bonaventure</li>
            </ul>	
            <br>
            <ul class="matchup">
              <li class="team team-top" id="correct">Colorado</li>
              <li class="team team-bottom" id="correct">Florida State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">BYU</li>
              <li class="team team-bottom" id="wrong">Texas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">UConn</li>
              <li class="team team-bottom" id="correct">Alabama</li>
            </ul>											
          </div>	<!-- END ROUND TWO -->
          <div class="round round-three current">
            <div class="round-details">Sweet 16</div>		
            <ul class="matchup">
              <li class="team team-top" id="correct">Gonzaga</li>
              <li class="team team-bottom" id="wrong">Virginia</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">USC</li>
              <li class="team team-bottom" id="wrong">Iowa</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Michigan</li>
              <li class="team team-bottom" id="correct">Florida State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Texas</li>
              <li class="team team-bottom" id="correct">Alabama</li>
            </ul>											
          </div>	<!-- END ROUND THREE -->		
        </div> 
        <div class="champion current">
            <div class="semis-l">
              <div class="round-details">Elite Eight</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Gonzaga</li>
                <li class="team team-bottom" id="wrong">Iowa</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Baylor</li>
                <li class="team team-bottom" id="wrong">Ohio State</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Michigan</li>
                <li class="team team-bottom" id="wrong">Alabama</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Illinois</li>
                <li class="team team-bottom" id="correct">Houston</li>
              </ul>
            </div>
            <div class="final">
              <div class="round-details">Final Four</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Iowa</li>
                <li class="team team-bottom" id="wrong">Michigan</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Ohio State</li>
                <li class="team team-bottom" id="wrong">Illinois</li>
              </ul>
            </div>
            <div class="semis-r">		
              <div class="round-details">Championship</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Michigan</li>
                <li class="team team-bottom" id="wrong">Illinois</li>
              </ul>
            </div>	
          </div>
	        <div class="split split-two">
          <div class="round round-three current">
            <div class="round-details">Sweet 16</div>						
            <ul class="matchup">
              <li class="team team-top" id="correct">Baylor</li>
              <li class="team team-bottom" id="correct">Villanova</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Arkansas</li>
              <li class="team team-bottom" id="wrong">Ohio State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Illinois</li>
              <li class="team team-bottom" id="wrong">Tennessee</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">San Diego</li>
              <li class="team team-bottom" id="correct">Houston</li>
            </ul>											
          </div>	<!-- END ROUND THREE -->	
          <div class="round round-two current">
            <div class="round-details">Second Round</div>						
            <ul class="matchup">
              <li class="team team-top" id="correct">Baylor</li>
              <li class="team team-bottom" id="correct">Wisconsin</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Villanova</li>
              <li class="team team-bottom" id="wrong">Purdue</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Texas Tech</li>
              <li class="team team-bottom" id="correct">Arkansas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Virginia Tech</li>
              <li class="team team-bottom" id="wrong">Ohio State</li>
            </ul>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Illionois</li>
              <li class="team team-bottom" id="correct">Loyola</li>
            </ul>	
            <br>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Tennessee</li>
              <li class="team team-bottom" id="correct">Oklahoma</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">San Diego</li>
              <li class="team team-bottom" id="correct">West Virginia</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="correct">Rutgers</li>
              <li class="team team-bottom" id="correct">Houston</li>
            </ul>																
          </div>	<!-- END ROUND TWO -->
          <div class="round round-one current">
            <div class="round-details">First Round</div>
            <ul class="matchup">
				      <li class="team team-top">Baylor</li>
				      <li class="team team-bottom lost">Hartford</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">North Carolina</li>
				      <li class="team team-bottom">Wisconsin</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Villanova</li>
				      <li class="team team-bottom">Winthrop</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Purdue</li>
				      <li class="team team-bottom">North Texas</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">Texas Tech</li>
				      <li class="team team-bottom">Utah State</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Arkansas</li>
				      <li class="team team-bottom">Colgate</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Florida</li>
				      <li class="team team-bottom">Virginia Tech</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Ohio State</li>
				      <li class="team team-bottom">Oral Roberts</li>
			      </ul>
            <ul class="matchup">
				      <li class="team team-top">Illinois</li>
				      <li class="team team-bottom">Drexel</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">Loyola</li>
				      <li class="team team-bottom">Georgia Tech</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Tennessee</li>
				      <li class="team team-bottom">Oregon State</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Oklahoma State</li>
				      <li class="team team-bottom">Liberty</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">San Diego State</li>
				      <li class="team team-bottom">Syracuse</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">West Virginia</li>
				      <li class="team team-bottom">Morehead</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Clemson</li>
				      <li class="team team-bottom">Rutgers</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Houston</li>
				      <li class="team team-bottom">Cleveland State</li>
			      </ul>											
          </div>	<!-- END ROUND ONE -->          				
	      </div>
	    </div>
	</section>
</div>

<div id="Team Jersey Color" class="tabcontent">
    <section id="bracket">
    <div class="round-details">32/62 Correctly Predicted</div>
	  <div class="container">
	    <div class="split split-one">
		    <div class="round round-one current">
			    <div class="round-details">First Round</div>
			      <ul class="matchup">
				      <li class="team team-top">Gonzaga</li>
				      <li class="team team-bottom lost">Norfolk State</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">Oklahoma</li>
				      <li class="team team-bottom">Missouri</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Creighton</li>
				      <li class="team team-bottom">UCSB</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Virginia</li>
				      <li class="team team-bottom">Ohio</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">USC</li>
				      <li class="team team-bottom">Drake</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Kansas</li>
				      <li class="team team-bottom">Eastern Washington</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Oregon</li>
				      <li class="team team-bottom">VCU</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Iowa</li>
				      <li class="team team-bottom">Grand Canyon</li>
			      </ul>
            <ul class="matchup">
				      <li class="team team-top">Michigan</li>
				      <li class="team team-bottom">Texas Southern</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">LSU</li>
				      <li class="team team-bottom">St. Bonaventure</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Colorado</li>
				      <li class="team team-bottom">Georgetown</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Florida State</li>
				      <li class="team team-bottom">UNC Greensboro</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">BYU</li>
				      <li class="team team-bottom">UCLA</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Texas</li>
				      <li class="team team-bottom">Abilene Christian</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">UConn</li>
				      <li class="team team-bottom">Maryland</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Alabama</li>
				      <li class="team team-bottom">Iona</li>
			      </ul>											
		      </div>	<!-- END ROUND ONE -->
          <div class="round round-two current">
            <div class="round-details">Second Round</div>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Gonzaga</li>
              <li class="team team-bottom" id="correct">Oklahoma</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Creighton</li>
              <li class="team team-bottom" id="wrong">Virginia</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Drake</li>
              <li class="team team-bottom" id="correct">Kansas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">VCU</li>
              <li class="team team-bottom" id="correct">Iowa</li>
            </ul>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Michigan</li>
              <li class="team team-bottom" id="wrong">St. Bonaventure</li>
            </ul>	
            <br>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Georgetown</li>
              <li class="team team-bottom" id="correct">Florida State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">BYU</li>
              <li class="team team-bottom" id="wrong">Texas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">UConn</li>
              <li class="team team-bottom" id="correct">Alabama</li>
            </ul>											
          </div>	<!-- END ROUND TWO -->
          <div class="round round-three current">
            <div class="round-details">Sweet 16</div>		
            <ul class="matchup">
              <li class="team team-top" id="correct">Gonzaga</li>
              <li class="team team-bottom" id="wrong">Virginia</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">USC</li>
              <li class="team team-bottom" id="wrong">Iowa</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Michigan</li>
              <li class="team team-bottom" id="wrong">Georgetown</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">BYU</li>
              <li class="team team-bottom" id="wrong">UConn</li>
            </ul>											
          </div>	<!-- END ROUND THREE -->		
        </div> 
        <div class="champion current">
            <div class="semis-l">
              <div class="round-details">Elite Eight</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Gonzaga</li>
                <li class="team team-bottom" id="wrong">Iowa</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">North Carolina</li>
                <li class="team team-bottom" id="wrong">Utah State</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Georgetown</li>
                <li class="team team-bottom" id="wrong">BYU</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Liberty</li>
                <li class="team team-bottom" id="correct">Houston</li>
              </ul>
            </div>
            <div class="final">
              <div class="round-details">Final Four</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Gonzaga</li>
                <li class="team team-bottom" id="wrong">Georgetown</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">North Carolina</li>
                <li class="team team-bottom" id="correct">Houston</li>
              </ul>
            </div>
            <div class="semis-r">		
              <div class="round-details">Championship</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Georgetown</li>
                <li class="team team-bottom" id="wrong">Houston</li>
              </ul>
            </div>	
          </div>
	        <div class="split split-two">
          <div class="round round-three current">
            <div class="round-details">Sweet 16</div>						
            <ul class="matchup">
              <li class="team team-top" id="correct">North Carolina</li>
              <li class="team team-bottom" id="correct">Villanova</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Utah State</li>
              <li class="team team-bottom" id="wrong">Oral Roberts</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Illinois</li>
              <li class="team team-bottom" id="wrong">Liberty</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">San Diego</li>
              <li class="team team-bottom" id="correct">Houston</li>
            </ul>											
          </div>	<!-- END ROUND THREE -->	
          <div class="round round-two current">
            <div class="round-details">Second Round</div>						
            <ul class="matchup">
              <li class="team team-top" id="correct">Hartford</li>
              <li class="team team-bottom" id="correct">North Carolina</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Villanova</li>
              <li class="team team-bottom" id="wrong">North Texas</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Utah State</li>
              <li class="team team-bottom" id="correct">Colgate</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Florida</li>
              <li class="team team-bottom" id="wrong">Oral Roberts</li>
            </ul>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Drexel</li>
              <li class="team team-bottom" id="correct">Georgia Tech</li>
            </ul>	
            <br>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Tennessee</li>
              <li class="team team-bottom" id="correct">Liberty</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">San Diego</li>
              <li class="team team-bottom" id="correct">Morehead State</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="correct">Rutgers</li>
              <li class="team team-bottom" id="correct">Houston</li>
            </ul>																
          </div>	<!-- END ROUND TWO -->
          <div class="round round-one current">
            <div class="round-details">First Round</div>
            <ul class="matchup">
				      <li class="team team-top">Baylor</li>
				      <li class="team team-bottom lost">Hartford</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">North Carolina</li>
				      <li class="team team-bottom">Wisconsin</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Villanova</li>
				      <li class="team team-bottom">Winthrop</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Purdue</li>
				      <li class="team team-bottom">North Texas</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">Texas Tech</li>
				      <li class="team team-bottom">Utah State</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Arkansas</li>
				      <li class="team team-bottom">Colgate</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Florida</li>
				      <li class="team team-bottom">Virginia Tech</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Ohio State</li>
				      <li class="team team-bottom">Oral Roberts</li>
			      </ul>
            <ul class="matchup">
				      <li class="team team-top">Illinois</li>
				      <li class="team team-bottom">Drexel</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">Loyola</li>
				      <li class="team team-bottom">Georgia Tech</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Tennessee</li>
				      <li class="team team-bottom">Oregon State</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Oklahoma State</li>
				      <li class="team team-bottom">Liberty</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">San Diego State</li>
				      <li class="team team-bottom">Syracuse</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">West Virginia</li>
				      <li class="team team-bottom">Morehead</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Clemson</li>
				      <li class="team team-bottom">Rutgers</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Houston</li>
				      <li class="team team-bottom">Cleveland State</li>
			      </ul>											
          </div>	<!-- END ROUND ONE -->          				
	      </div>
	    </div>
	</section>
  
</div>

<div id="Crowd Choice" class="tabcontent">
    <section id="bracket">
    <div class="round-details">33/62 Correctly Predicted</div>
	  <div class="container">
	    <div class="split split-one">
		    <div class="round round-one current">
			    <div class="round-details">First Round</div>
			      <ul class="matchup">
				      <li class="team team-top">Gonzaga</li>
				      <li class="team team-bottom lost">Norfolk State</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">Oklahoma</li>
				      <li class="team team-bottom">Missouri</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Creighton</li>
				      <li class="team team-bottom">UCSB</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Virginia</li>
				      <li class="team team-bottom">Ohio</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">USC</li>
				      <li class="team team-bottom">Drake</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Kansas</li>
				      <li class="team team-bottom">Eastern Washington</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Oregon</li>
				      <li class="team team-bottom">VCU</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Iowa</li>
				      <li class="team team-bottom">Grand Canyon</li>
			      </ul>
            <ul class="matchup">
				      <li class="team team-top">Michigan</li>
				      <li class="team team-bottom">Texas Southern</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">LSU</li>
				      <li class="team team-bottom">St. Bonaventure</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Colorado</li>
				      <li class="team team-bottom">Georgetown</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Florida State</li>
				      <li class="team team-bottom">UNC Greensboro</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">BYU</li>
				      <li class="team team-bottom">UCLA</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Texas</li>
				      <li class="team team-bottom">Abilene Christian</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">UConn</li>
				      <li class="team team-bottom">Maryland</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Alabama</li>
				      <li class="team team-bottom">Iona</li>
			      </ul>											
		      </div>	<!-- END ROUND ONE -->
          <div class="round round-two current">
            <div class="round-details">Second Round</div>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Gonzaga</li>
              <li class="team team-bottom" id="correct">Oklahoma</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Creighton</li>
              <li class="team team-bottom" id="wrong">Virginia</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">USC</li>
              <li class="team team-bottom" id="correct">Kansas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="correct">Oregon</li>
              <li class="team team-bottom" id="correct">Iowa</li>
            </ul>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Michigan</li>
              <li class="team team-bottom" id="correct">LSU</li>
            </ul>	
            <br>
            <ul class="matchup">
              <li class="team team-top" id="correct">Colorado</li>
              <li class="team team-bottom" id="correct">Florida State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">BYU</li>
              <li class="team team-bottom" id="wrong">Texas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">UConn</li>
              <li class="team team-bottom" id="correct">Alabama</li>
            </ul>											
          </div>	<!-- END ROUND TWO -->
          <div class="round round-three current">
            <div class="round-details">Sweet 16</div>		
            <ul class="matchup">
              <li class="team team-top" id="correct">Gonzaga</li>
              <li class="team team-bottom" id="wrong">Virginia</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Kansas</li>
              <li class="team team-bottom" id="wrong">Iowa</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Michigan</li>
              <li class="team team-bottom" id="correct">Florida State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Texas</li>
              <li class="team team-bottom" id="correct">Alabama</li>
            </ul>											
          </div>	<!-- END ROUND THREE -->		
        </div> 
        <div class="champion current">
            <div class="semis-l">
              <div class="round-details">Elite Eight</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Gonzaga</li>
                <li class="team team-bottom" id="wrong">Iowa</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Baylor</li>
                <li class="team team-bottom" id="wrong">Ohio State</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Michigan</li>
                <li class="team team-bottom" id="wrong">Alabama</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="wrong">Illinois</li>
                <li class="team team-bottom" id="correct">Houston</li>
              </ul>
            </div>
            <div class="final">
              <div class="round-details">Final Four</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Gonzaga</li>
                <li class="team team-bottom" id="wrong">Michigan</li>
              </ul>
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Baylor</li>
                <li class="team team-bottom" id="wrong">Illinois</li>
              </ul>
            </div>
            <div class="semis-r">		
              <div class="round-details">Championship</div>		
              <ul class ="matchup championship">
                <li class="team team-top" id="correct">Gonzaga</li>
                <li class="team team-bottom" id="wrong">Illinois</li>
              </ul>
            </div>	
          </div>
	        <div class="split split-two">
          <div class="round round-three current">
            <div class="round-details">Sweet 16</div>						
            <ul class="matchup">
              <li class="team team-top" id="correct">Baylor</li>
              <li class="team team-bottom" id="wrong">Purdue</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Arkansas</li>
              <li class="team team-bottom" id="wrong">Ohio State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">Illinois</li>
              <li class="team team-bottom" id="wrong">Oklahoma State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">West Virginia</li>
              <li class="team team-bottom" id="correct">Houston</li>
            </ul>											
          </div>	<!-- END ROUND THREE -->	
          <div class="round round-two current">
            <div class="round-details">Second Round</div>						
            <ul class="matchup">
              <li class="team team-top" id="correct">Baylor</li>
              <li class="team team-bottom" id="wrong">North Carolina</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Villanova</li>
              <li class="team team-bottom" id="wrong">Purdue</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="correct">Texas Tech</li>
              <li class="team team-bottom" id="correct">Arkansas</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="correct">Florida</li>
              <li class="team team-bottom" id="wrong">Ohio State</li>
            </ul>			
            <ul class="matchup">
              <li class="team team-top" id="correct">Illionois</li>
              <li class="team team-bottom" id="correct">Loyola</li>
            </ul>	
            <br>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Tennessee</li>
              <li class="team team-bottom" id="correct">Oklahoma State</li>
            </ul>	
            <ul class="matchup">
              <li class="team team-top" id="wrong">San Diego</li>
              <li class="team team-bottom" id="correct">West Virginia</li>
            </ul>
            <ul class="matchup">
              <li class="team team-top" id="wrong">Clemson</li>
              <li class="team team-bottom" id="correct">Houston</li>
            </ul>																
          </div>	<!-- END ROUND TWO -->
          <div class="round round-one current">
            <div class="round-details">First Round</div>
            <ul class="matchup">
				      <li class="team team-top">Baylor</li>
				      <li class="team team-bottom lost">Hartford</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">North Carolina</li>
				      <li class="team team-bottom">Wisconsin</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Villanova</li>
				      <li class="team team-bottom">Winthrop</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Purdue</li>
				      <li class="team team-bottom">North Texas</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">Texas Tech</li>
				      <li class="team team-bottom">Utah State</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Arkansas</li>
				      <li class="team team-bottom">Colgate</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Florida</li>
				      <li class="team team-bottom">Virginia Tech</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Ohio State</li>
				      <li class="team team-bottom">Oral Roberts</li>
			      </ul>
            <ul class="matchup">
				      <li class="team team-top">Illinois</li>
				      <li class="team team-bottom">Drexel</li>
			      </ul>
		      	<ul class="matchup">
				      <li class="team team-top">Loyola</li>
				      <li class="team team-bottom">Georgia Tech</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Tennessee</li>
				      <li class="team team-bottom">Oregon State</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Oklahoma State</li>
				      <li class="team team-bottom">Liberty</li>
			      </ul>			
			      <ul class="matchup">
				      <li class="team team-top">San Diego State</li>
				      <li class="team team-bottom">Syracuse</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">West Virginia</li>
				      <li class="team team-bottom">Morehead</li>
			      </ul>	
			      <ul class="matchup">
				      <li class="team team-top">Clemson</li>
				      <li class="team team-bottom">Rutgers</li>
			      </ul>
			      <ul class="matchup">
				      <li class="team team-top">Houston</li>
				      <li class="team team-bottom">Cleveland State</li>
			      </ul>											
          </div>	<!-- END ROUND ONE -->          				
	      </div>
	    </div>
	</section>
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


And this field doesn't gate-keep either. 

With publicly available packages such as [sklearn](https://scikit-learn.org/stable/), [keras](https://keras.io/), and [tensorflow](https://www.tensorflow.org/) the bar to start using sophisticated algorithms has never been lower.

In conjunction with the availability of [open-source datasets](https://www.kaggle.com/datasets), it seems that every field is now open to modeling. 

This field promises: not everyone can be an expert, but with the right tools and resources, they can create models that perform like experts. 
</details>

<details markdown="1">
<summary style="display:list-item"><span>American Basketball</span></summary> 

But can we really explore a field for which we have no "domain knowledge" of and create predictions that suprass the foresight of experts? The term "domain knowledge" refers to the traditional method of becoming acquintated with any particular field: recieving an accredited degree, consulting the knowledge of the past using textbooks, or by simply being an aged observer of the phenomenon. 

This question is especially relevant when we deal with human-centered fields.

For example, within the neary 100-year history of the NCAA's college basketball tournemant "March Madness", a 16-seeded team has never won against a 1-seeded team. That is, until 2018. 

<figure>
  <img src="images\header-1.jpg" id="large-image">  
    <figcaption>UMBC v. Virginia</figcaption>
</figure>

Could an algorithm have predicted this performance, even though no basketball "expert" could?

In 2018 I trained a classifier on team-ranking data from basketball enthusiasts. It gave UMBC a 2% chance of victory. Perhaps a "better" model would have expressed the historical impossibility with greater sufficiency and given it a 0% chance. 

This year, my methodology hasn't changed. Instead, I take a step back and ask: "do I even bother modelling a college basketball when I myself have never casually watched sports?"

So, I compare my work to the following "non-data driven" bracket predictions:

- the winner always has the more popular [team color](https://www.spoonflower.com/americas_true_colors). 
- the winner is chosen by the [wisdom of crowds](https://fantasy.espn.com/tournament-challenge-bracket/2021/en/nationalBracket)

Through this comparison, I begin asking: 

- Is it just as bad to guess (or forgo data when making predictions) than create a model for a poorly-understood field? 
- Does all data point to an interesting & predictive model?
- Are there fields where algorithms will never be as good as the opinion of "experts"
- Do experts even exist when it comes to "prediction"?
</details>

## Meme tax 

<img src="images\4c7r0e.jpg" id="small-image"/>