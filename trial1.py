import Algorithmia
input = {
	"image": "data://kornosk130/deeplearning/input.jpeg" # Set location of your own image
}
client = Algorithmia.client('simJAXLxj1N4qho8CM+WdCuY2bP1') # Insert your own API key
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5') # Name of algorithm which we will use
print(algo.pipe(input))