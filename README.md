[![AWS - Flask ELastic Beanstalk](https://github.com/louis-mouline/Flask-Elastic-Beanstalk/actions/workflows/aws_workflow.yml/badge.svg)](https://github.com/louis-mouline/Flask-Elastic-Beanstalk/actions/workflows/aws_workflow.yml)

# Flask-Elastic-Beanstalk

The objective is to build a Flask Application that is Continuously Deployed using AWS Elastic Beanstalk.

![eb-deploy](https://user-images.githubusercontent.com/58792/106804626-a3a81900-6633-11eb-9cf6-54c24af6827f.png)


### Deploy via AWs Cloud9 + AWS Code Build

*You can refer to tutorial [here as well for Flask EB](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)*

1.  check out this repo and cd into it
2.  create a python virtualenv and source it and run `make all`

`python3 -m venv ~/.virtual`
`source ~/.virtual/bin/activate`
`make all`

*Note, that awsebcli is installed via requirements*

3. initialize new eb app

`eb init -p python-3.7 flask-continuous-delivery --region us-east-1`

*Optional `eb init` again to create ssh keys*

4. Create remote eb instance

`eb create flask-continuous-delivery-env`

5.  Setup AWS Code Build Project

[View Sample `buildspec.yml` Config Here](https://github.com/noahgift/Flask-Elastic-Beanstalk/blob/main/buildspec.yml)
