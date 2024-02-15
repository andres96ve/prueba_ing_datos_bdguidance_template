all: dvdrental.tar

dvdrental.zip:
	curl -L https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip -o $@

dvdrental.tar: dvdrental.zip
	unzip $<
	touch $@