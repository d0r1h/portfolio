# Portfolio
A Web Portfolio to showcase the achievements.


How to ----

        1. Go to the project dir in the terminal and type this command
            python -m venv ll_env { this will create Python virtual env, So any activity that you will do
            in this env, won't be affecting your real env/your computer.}
        2. portfolio_env/Scripts/activate     To activate the virtual env 
        3. pip install flask   To install flask
                python -c "import flask; print(flask.__version__)"   to check if is is installed properly.
        4. Created hello.py and added the code for handling http response. 
        5.  to run the web application you first tell flask where to find application file(hello.py)
            set PORTFOLIO_APP=hello
            set PORTFOLIO_ENV=development    run in developmetn mode
            flask run   run the application