//Prevents resizing because my design skills are awful
//and its not responsive
window.onresize = function() {
    window.resizeTo(566, 639);
};

//Upload function
function uploadFile() {
    var input = document.getElementById('fileInput'); //Get fileInput element
    var file = input.files[0]; //Getting the file
    eel.upload_file(file.name) //pass file to python side
}

//Set settings
function setSettings() {
    //get html elements and their values
    let width = document.getElementById('width').value;
    let height = document.getElementById('height').value;
    let frame_rate = document.getElementById('frame-rate').value;
    let conf = document.getElementById('conf').value;

    eel.setup_settings(width, height, frame_rate, conf); //pass to python class
}

//Reset settings
function resetSettings() {
    eel.reset_settings(); //reset settings in the python class
}

//Message box - General
function updateMessage(msg) {
    document.getElementById('message').innerText = msg;
}

//Message box - Settings
function updateSettingsMessage(msg) {
    document.getElementById('settings-message').innerText = msg;
}

//Open predictions folder
function openResults() {
    eel.open_predictions();
}

//Open upload folder
function openUpload() {
    eel.open_upload();
}

//Pick YOLOv8n
function pickYOLOv8n() {
    eel.switch_v8n();
}

//Pick YOLOv8x
function pickYOLOv8x() {
    eel.switch_v8x();
}

//Make functions callable on the python side
eel.expose(setSettings);
eel.expose(resetSettings);
eel.expose(updateMessage);
eel.expose(updateSettingsMessage);