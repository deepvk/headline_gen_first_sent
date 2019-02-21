# First Sentence Baseline
First Sentence Baseline for Headline Generation shared task on Dialogue 2019

This baseline just cut off the first sentence in a news article body and treat as a hypothesis for a article title.

To use it: 
1) fork and/or clone the repo;
2) login into shared task private registry with command `sudo docker login headlinegen.vkpartner.ru:5001`
3) build docker image with command `sudo docker build --tag headlinegen.vkpartner.ru:5001/{your_token} .`
4) push docker image to registry with command `sudo docker push headlinegen.vkpartner.ru:5001/{your_token}`
5) click __Валидировать__ on [shared task website](https://headlinegen.vkpartner.ru/submit_page).
