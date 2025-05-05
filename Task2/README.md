This is a student project:


Create rich visualizations using an implementation of the grammar of graphics:

     0. Download the datasets (LLM battles.zip) from the course website

The dataset contains the results of game tournaments between LLMs

The game is similar to Among Us and the LLMs played either as Crewmates (4 good guys) or Impostors (1 bad guy)

The tournament consisted of 10 games between each pair of LLMs (5 games of the same LLM against itself in different roles); a total of 640 games

The data is spread between several files describing: 
* the type of LLM (Claude, GPT-4, Gemini, Llama), 
* size of LLM (large, small), 
* number of wins in different roles (Crewmate, Impostor), 
* the number of tokens used (token ≈ word, directly related to price), 
* number and type of persuasions used during in-game discussion (persuasion techniques taken from rhetoric and psychology)
* etc.

The experiments were designed to verify how proficient LLMs are at persuasion even when not trained or not prompted to use particular persuasion techniques. Which persuasion techniques do LLMs use? How often? Does persuasion depend on LLM type or size? Do particular LLMs win more often in persuasion games when put against each other?

The visualization should probably try to answer the above research questions

Task:
* Sketch at least one of the ideas
* Prepare three sets of preliminary (static) plots
* The plots should be prepared using an implementation of the grammar of graphics in R or Python (ggplot2, plotnine, altair)
* Select one of the ideas and prepare a final presentation-ready plot also with a grammar of graphics implementation
