import torch
from flask import Flask, app, request, jsonify
from fastapi import FastAPI

# Save the model
torch.save(model.state_dict(), 'model.pth')#this contains the weights of the model and biases

#save entire model
torch.save(model, 'entire_model.pth')#this contains the architecture of the model                   

#load the model
model = TheModelClass(*args, **kwargs) #initialize the model class
model.load_state_dict(torch.load('model.pth')) #load the weights and biases into the model
model.eval() #set the model to evaluation mode

model = torch.load('entire_model.pth') #load the entire model including architecture and weights

#deploying the model
scripted_model = torch.jit.script(model) #convert the model to TorchScript
torch.jit.save(scripted_model, 'scripted_model.pt') #save the TorchScript model

#tracing the model
example_input = torch.rand(1, 3, 224, 224) #create an example input tensor
traced_model = torch.jit.trace(model, example_input) #trace the model with an example input
torch.jit.save(traced_model, 'traced_model.pt') #save the traced model

#onnx 
torch.onnx.export(model, example_input, 'model.onnx', export_params=True, opset_version=10, do_constant_folding=True, input_names=['input'], output_names=['output'], dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}) #export the model to ONNX format

#serving pytorch model using torchserve, fastapi, flask, django, etc.

app = Flask(__name__)
model=TheModelClass(*args, **kwargs) #initialize the model class
model.load_state_dict(torch.load('model.pth')) #load the weights and biases into the
model.eval() #set the model to evaluation mode

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True) #get the input data from the request
    input_tensor = torch.tensor(data['input']) #convert the input data to a tensor
    with torch.no_grad(): #disable gradient calculation for inference
        output = model(input_tensor) #get the model output
    return jsonify({'output': output.tolist()}) #return the output as a JSON response

if __name__ == '__main__':
    app.run(debug=True) #run the Flask app in debug mode

#serving using fastapi
app = FastAPI()
model=TheModelClass(*args, **kwargs) #initialize the model class
model.load_state_dict(torch.load('model.pth')) #load the weights and biases into the
model.eval() #set the model to evaluation mode

@app.post('/predict')
async def predict(data: dict):
    input_tensor = torch.tensor(data['input']) #convert the input data to a tensor
    with torch.no_grad(): #disable gradient calculation for inference
        output = model(input_tensor) #get the model output
    return {'output': output.tolist()} #return the output as a JSON response
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

    