file_name=./sneaker-recognition-ai/static/style.css

timestamp=$(stat -c %Y $file_name)

cp -v $file_name $file_name?q=$timestamp
