clear-dist:
	rm dist/* | true

sdist:
	python setup.py sdist

pypi: clear-dist sdist
	twine upload dist/*
