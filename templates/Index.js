var up = 'none';
var down = 'none';
var left = 'none';
var right = 'none';
var camUp = 'none';
var camDown = 'none';
var camLeft = 'none';
var camRight = 'none';
var camReset = 'none';
document.addEventListener('keydown', function(event) {
    if(event.keyCode == 37) {
        if(left!="pressed"){
            left="pressed"
            let data = {'steering': "left"};
            
            fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
    else if(event.keyCode == 39) {
        if (right!="pressed"){
            right="pressed"
            let data = {'steering': "right"};

            fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
    else if(event.keyCode == 38) {
        if(up!='pressed'){
            up="pressed"
            let data = {'direction': 'forward'};
            
            fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
            up='pressed'
        }
    }
    else if(event.keyCode == 40) {
        if (down!="pressed"){
            down="pressed"
            let data = {'direction': 'backward'};

            fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
    
});

document.addEventListener('keyup', function(event) {
    if(event.keyCode == 37) {
        left="none"
        let data = {'steering': "straight"};
        
        fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    else if(event.keyCode == 39) {
        right="none"
        let data = {'steering': 'straight'};

        fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    else if(event.keyCode == 38) {
        up="none"
        let data = {"direction": "stopped"}

        fetch("/button", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    else if(event.keyCode == 40) {
        down="none"
        let data = {"direction": "stopped"}

        fetch("/button", {
            method: "POST", 
            body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    
});
document.addEventListener('keydown', function(event) {
    if(event.keyCode == 87) {
        if(camUp!="pressed"){
            camUp="pressed"
            let data = {'CameraVertical': "Up"};
            
            fetch("/cameraVertical", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
    else if(event.keyCode == 83) {
        if (camDown!="pressed"){
            camDown="pressed"
            let data = {'CameraVertical': "Down"};

            fetch("/cameraVertical", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
    else if(event.keyCode == 65) {
        if(camLeft!='pressed'){
            camLeft="pressed"
            let data = {'CameraHorizontal': 'Left'};
            
            fetch("/cameraHorizontal", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
            up='pressed'
        }
    }
    else if(event.keyCode == 68) {
        if (camRight!="pressed"){
            camRight="pressed"
            let data = {'CameraHorizontal': 'Right'};

            fetch("/cameraHorizontal", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
    
});
document.addEventListener('keyup', function(event) {
    if(event.keyCode == 87) {
        camUp="none"
        let data = {'CameraVertical': "Stopped"};
        
        fetch("/cameraVertical", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    else if(event.keyCode == 83) {
        camDown="none"
        let data = {'CameraVertical': "Stopped"};
        fetch("/cameraVertical", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    else if(event.keyCode == 65) {
        camLeft="none"
        let data = {'CameraHorizontal': "Stopped"};
        fetch("/cameraHorizontal", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    else if(event.keyCode == 68) {
        camRight="none"
        let data = {'CameraHorizontal': "Stopped"};
        fetch("/cameraHorizontal", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
    
});
document.addEventListener('keydown', function(event) {

    if(event.keyCode == 82) {
        if (camReset!="pressed"){
	    camRight="pressed"
            let data = {'CameraReset': 'true'};
            fetch("/cameraReset", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
        }
    }
});
document.addEventListener('keyup', function(event) {
    if(event.keyCode == 82) {
        camReset="none"
        let data = {'CameraReset': "false"};
        
        //fetch("/cameraReset", {method: "POST", body: JSON.stringify(data)}).then(res => {console.log("Request complete! response:", data);})
    }
});
