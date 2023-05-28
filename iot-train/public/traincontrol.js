
var selected_train = 0

var max_speed = 10;

let speed = [0, 0];
// direction 1=fwd, 0=stop, -1=rev
let direction = [0, 0]

// Warning messages - for calc expiry time
let warn_msg_expiry = [0, 0];
// How long to display messages (in ms)
// Only reviewed when there is a change in speed etc.
var warn_expiry_length = 3000;


// Speed rotation angles (dial display)
let speed_angle = [-147, -120, -90, -60, -39, 0, 28, 60, 90, 119, 142]


// direction is 0 = stop, 1 = fwd, 2 = rev
// if direction is stop then speed value ignored

// call back function from ajax code
function updateStatus (data) {
    // Set status message
    $('#status').html(data);
}


// Updates the train with current speed and direction (based on global variable)
function updateTrain (train_id) {
        // if direction is 0 (stop) then also reset speed to 0
        if (direction[train_id] == 0) speed[train_id] = 0;
    $.get('control', {speed: speed[train_id], train: train_id, direction: direction[train_id]}, updateStatus);
    // Move this to call back function?
    viewDisplay (train_id);
}


function setSpeed (speed_val, train_id, direction_str) {
    $.get('/control', {speed: speed_val, train: train_id, direction: direction_str}, updateStatus);
    // Move this to call back function
    viewDisplay (train_id);
}

// Updates all displays
function viewDisplay (train_id) {
         viewMsg (train_id);
     viewSpeed (train_id);
         viewDirection (train_id);
}


// Removes messages that have expired
// Does not add message
function viewMsg (train_id) {
        // not displaying any message (or message is non expirying)
        if (warn_msg_expiry[train_id] == 0) return;
        // expired message
        if (warn_msg_expiry[train_id] < Date.now()) {
              warn_msg_expiry[train_id] = 0;
                $( '#message'+train_id ).html("&nbsp;");
        }

}

function viewSpeed (train_id) {
     $( "#speeddisplay"+train_id ).rotate({animateTo:speed_angle[speed[train_id]]});
}

function viewDirection (train_id) {
    if (direction[train_id] == 1) {
        $( "#reverser"+train_id ).attr("src", "public/reverser-fwd.png");
    }
    if (direction[train_id] == -1) {
        $( "#reverser"+train_id ).attr("src", "public/reverser-rev.png");
    }
    if (direction[train_id] == 0) {
        $( "#reverser"+train_id ).attr("src", "public/reverser-stop.png");
    }
}


/* String functions interpret strings and convert to regular functions */
function mapString (string_val) {
        // last character is train_id
    instruction = string_val.substring(0, string_val.length-1);
        train_id = parseInt(string_val.substring(string_val.length-1));
        // Direction - can only move one step at a time (eg. if forward must go stop before reverse)
    if (instruction == "forward") {
            if (direction[train_id] >= 0) direction[train_id] = 1;
            else {
            direction[train_id] = 0;
            // also set speed to 0
            speed[train_id] = 0;
            }
        }
        else if (instruction == "reverse") {
            if (direction[train_id] <= 0) direction[train_id] = -1;
            else {
                direction[train_id] = 0;
                speed[train_id] = 0;
                }
        }
    else if (instruction == "stop") direction[train_id] = 0;
        // Speed
        else if (instruction == "faster") {
          // if direction is 0 then give warning and set speed to 0
            if (direction[train_id] == 0) warnStop(train_id);
            else speed[train_id] = validateSpeed (speed[train_id]+1);
            }
        else if (instruction == "slower") {
            if (direction[train_id] == 0) warnStop(train_id);
            else speed[train_id] = validateSpeed (speed[train_id]-1);
            }

    updateTrain (train_id);
}

// Issue warning that haven't moved direction lever
function warnStop(train_id){
    warn_msg_expiry[train_id] = Date.now() + warn_expiry_length;

    $( '#message'+train_id ).html("Direction lever needs to be moved first");
}

function validateSpeed (speed_val){
    if (speed_val > max_speed) {
      return max_speed;
        }
        else if (speed_val < 0) {
            return 0;
            }
        else return speed_val;
}


$(document).ready(function(e) {
    $('img[usemap]').rwdImageMaps();

    $('area').on('click', function() {
        mapString($(this).attr('alt'));
    });

    viewDisplay (0);
});
