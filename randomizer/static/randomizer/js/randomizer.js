
    console.log(typeof(nameArray));
    console.log(nameArray);

    var previousGroups = 0;  // # groups of previous freeze
    var moving = false;
    
    var numberStudents = nameArray.length;
    var interval;  // for the interval function that scrambles the names
    var attend = [];
    var no_pick = [];
    var groupMade = false;
    
    for(var n = 0; n < numberStudents; n++) {
        attend[n] = nameArray[n].fields.attend;
        no_pick[n] = nameArray[n].fields.do_not_pick;
        };
    var studentCol1 = document.getElementById('student-column1');
    var studentCol2 = document.getElementById('student-column2');
    var studentChoice = document.getElementById('student-choice');
    var vertGap = 30;
    var divChoice = document.createElement('div');                
    divChoice.id = "choicename";

    divChoice.innerHTML = " ";
    studentChoice.appendChild(divChoice);

    var setNames = function() {
        var h = 0;
        for(var n = 0; n < numberStudents; n++){   // place the names on the screen
            var w = 0;
            var divName = "floatName" + n;
            var names = nameArray[n].fields.nickname;
            var divTag = document.createElement('div');
            divTag.id = divName;
            divTag.innerHTML = names;
            divTag.style.position = "absolute";
            if (attend[n] == true) {
                divTag.style.textDecoration = "none";
            } else {
                divTag.style.textDecoration = "line-through";
                divTag.style.color = 'red';
            };
          
            h = n - Math.floor(n/15)*15;  // go back up to the top of the name column
            
            divTag.style.top = (10 + h * vertGap) + "px";
            //divTag.style.left  = (0 + w) + "px";
            divTag.style.fontSize = "14px";
            divTag.className = "randomFloat";
            divTag.onclick = boldText;
             
            if (Math.floor(n/15)+1 == 2) {
                studentCol2.appendChild(divTag);
            } else {
                studentCol1.appendChild(divTag);
            // attach to studentCol/'anchor'/parent element
            }; 
        };
    };
    setNames();
        
    $( "#go" ).click(function() {
        var N  // number of kids to be grouped after absent kids
        console.log("it's go time");
        moving = true;
        //clear the previous random name choice if there is one
        var divfc = document.getElementById('choicename');
        console.log(divfc);
        while(divfc.firstChild) {
            divfc.removeChild(divfc.firstChild);
        };
        
        // get the number of kids attending before clearGroups
        group = grouping(N);
        if (groupMade == true) {
            clearGroups(group[0]);
        }
        
        // move the floatNames divs around aka "the scrambler"
        var gotime = 1;
        interval = setInterval(function () {
            for(var i = 0; i < (numberStudents + 1); i++){
                var divName = "floatName" + i;
                if (attend[i] == true) {
                    $( "#" + divName ).css({
                        left: (Math.random()*500+300) + "px",
                        top: (Math.random()*350 + 40) + "px",
                        "font-size": "20px",
                    });
                };
            };
            gotime += 1;
            if (gotime > 100) {
                clearInterval(interval);
               }
        }, 500);
    });

    $( "#stop" ).click(function() {
        if (moving == true) {
            clearInterval(interval);
            choosePerson(0, numberStudents);
            setTimeout(clearDivs, 1000);
        };
        moving = false;
    });
    
    var clearDivs = function() {
        for(var i = 0; i < (numberStudents); i++) {
            divn = "floatName" + i;
            var elem = document.getElementById(divn);
            elem.remove();
            };
        setNames();
        };
        
    var clearGroups = function() {
        console.log(previousGroups);
        for (i = 0; i < previousGroups; i++) {  //remove the previous # of groups
            num = (i+1);
            var divn = "Group" + num.toString();
            var elem = document.getElementById(divn);
            elem.remove();
            };
        clearDivs();
        groupMade = false;
        }; 
        
        
    function choosePerson (min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        var rn = Math.floor(Math.random() * (max - min)) + min;
        console.log("is this working");
        while (attend[rn] == false || no_pick[rn] == true) {
            rn = Math.floor(Math.random() * (max - min)) + min;
            console.log("try again");
        };
        console.log(no_pick[rn]);
        console.log(attend[rn]);
        divChoice.innerHTML = nameArray[rn].fields.nickname;
        divChoice.style.position = "relative";
        divChoice.style.color = "blue";
        divChoice.style.fontWeight = "bold";
        divChoice.style.top = "10px";
        divChoice.style.left = "400px";
        studentChoice.appendChild(divChoice);
        };
                          
    function boldText(){
        var togname = this.id.split('floatName').join('');
        console.log(togname);
        var nam = nameArray[togname];
        console.log(nam);
        if (this.style.textDecoration == 'none') {
            this.style.textDecoration = 'line-through';
            this.style.color = 'red';
            attend[togname] = false;
        } else {
            this.style.textDecoration = 'none';
            this.style.color = 'black';
            attend[togname] = true;
        }
    };
        
    // knuff-shuffle to mix the list of students
    function shuffle() {
        var array = [];
        for (var n=0; n<numberStudents; n++) {
            array[n-0] = n;
        }
        var currentIndex = array.length
          , temporaryValue
          , randomIndex
          ;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

          // Pick a remaining element...
          randomIndex = Math.floor(Math.random() * currentIndex);
          currentIndex -= 1;

          // And swap it with the current element.
          temporaryValue = array[currentIndex];
          array[currentIndex] = array[randomIndex];
          array[randomIndex] = temporaryValue;
        }

        return array;
    }
    
    function grouping(e) {
        var ns = 0;
        // make sure to not count students that are away
        for (n=0; n < numberStudents; n++) {
            if (attend[n] == true) {
                ns++
            };
        };
        
        var extras = ns % e;
        var numGroups = [];
        var totalGroups = 0;
        var threeGroups = Math.floor(ns/e);
        
        if (extras != 0) {
            totalGroups = threeGroups + 1;
        } else {
            totalGroups = threeGroups;
        }
        return [totalGroups, ns]; 
    }
    
    function sort(groupsize) {
        var i = 0;
        var sortName  = [];
        var groupNumbers = [];
        var placeCount = 0;
        var groupDown = 0;
        var groupLeft = 0;
        groupMade = true;
        var studentAttend = 0;
        var leftOver = 0;
        
        // get the random order of students
        var groups = grouping(groupsize);
        previousGroups = groups[0];
        
        // shuffle the order of the students
        var studentOrder = shuffle(nameArray);
        
        // place the group headings
        for (i = 0; i < groups[0]; i++) {
            num = (i+1);
            divGroup = document.createElement('div');
            divGroup.innerHTML = "Group " + num.toString();
            divGroup.id = "Group" + num.toString();
            num = num*120-120;
            divGroup.style.width = "110px";
            divGroup.style.fontSize = "20px";
            divGroup.style.fontWeight = "bold";
            divGroup.style.color = "blue";
            divGroup.style.position = "absolute";
            divGroup.style.top = "100px";
            divGroup.style.left = num.toString() + "px";
            studentCol1.appendChild(divGroup);
        }
        
        // fill each row
        for (i = 0; i < numberStudents; i++) {
            var divName = "floatName" + studentOrder[i];
            var SO = studentOrder[i];
            console.log(document.getElementById(divName).parentNode);
            
            if (attend[SO] == true) {
                var stdId = document.getElementById(divName);
                stdId.parentNode.id = "studentCol1";
                studentCol1.appendChild(stdId);
                studentAttend++;
                stdId.style.fontSize = "20px";
                if (placeCount%groups[0] == 0) {  //check to see if we need a new row
                    groupDown = groupDown + 50;
                    groupLeft = 0;
                }
                $( "#" + divName ).animate({
                    left: ( 00 + groupLeft) + "px",
                    top: (100 + groupDown) + "px"
                }, 300 );
                groupLeft = groupLeft + 120;   // keep moving the names over
                placeCount++;
            } else {
                var stdId = document.getElementById(divName);
                stdId.parentNode.id = "studentCol1";
                studentCol1.appendChild(stdId);
                $("#" + divName ).css({
                    left: leftOver + "px",
                    top: "500px",
                } );
                leftOver = leftOver + 110; 
            }
        } 
    };
    
    $("#freezebutton").on("click", function() {
      let groupNumber = $("#freezeGroups").val();
      if (moving == true) {
            clearInterval(interval);
            setTimeout(sort(groupNumber), 1000);
        }
       moving = false;
      
      console.log("Random Group", groupNumber);
    });                
  
    