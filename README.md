# install dependencies
pip install -r requirements

# dir
cd SeleniumProjectPOM/

# to launch test: 
pytest -s -v -m "sanity" --html=Reports/report.html testCases/
(pytest -s -v -m "sanity or regression" --html=Reports/report.html testCases/)
(pytest -s -v -m "sanity and regression" --html=Reports/report.html testCases/
(pytest -s -v -m "regression" --html=Reports/report.html testCases/)


