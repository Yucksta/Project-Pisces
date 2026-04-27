function redundant (attempt, method1 = "log") {
    //this is really cool and I am suprised this worked, too bad the rest of the code still sucks.
    console.warn("This is a " + typeof(attempt) + " " + method1 + ":");
    console[method1](attempt);
}
redundant("*", "log");
redundant(3, "error");
let countvariablethatalsoneedstobethisway = 0;
let trying = 0;
let Atleast1iteratedarraywithaccessedandusedelementsinit = [];
let done206 = [false, "ThEre Are some new secrets in the consoLe 👀 👀 👀 👀 👀 👀!!"];
const documentaryelementalstatus = document.getElementById("test");
const documecondelementalstatus = document.getElementById("test3");

documentaryelementalstatus.onclick = function() {
    redundant("Button pressed.");
    if (done206[0] == false){
        done206[0] = true;
        redundant("Sucessfull press");
        redundant(document.cookie, "error");
        let lag = 0;
        while (countvariablethatalsoneedstobethisway < 100000) {
            const temporarylimitvariablethatwasenlargenedtoanunreasonablelengthforschoology = countvariablethatalsoneedstobethisway;
            function ComputerFrameUpdatingSoftwareDesignedToRepresentTheIllusionOfChioce () {
                lag++;
                documecondelementalstatus.textContent = "I am still in the process of making this website. I have to learn the programming languages: JavaScript, HTML, and CSS.\n" + (100000 - lag)
                documentaryelementalstatus.style.fontSize =  15 + Math.abs(Math.sin(temporarylimitvariablethatwasenlargenedtoanunreasonablelengthforschoology / 100) * 2) + "px";
                documentaryelementalstatus.style.color = "rgb(" + Math.abs(Math.sin(temporarylimitvariablethatwasenlargenedtoanunreasonablelengthforschoology / 100)) * 255 + ",0,0)";
            }
            if (countvariablethatalsoneedstobethisway % 1300 != 0 && countvariablethatalsoneedstobethisway % 294 != 0){
                setTimeout(ComputerFrameUpdatingSoftwareDesignedToRepresentTheIllusionOfChioce, countvariablethatalsoneedstobethisway * 5);
            }
            else if (countvariablethatalsoneedstobethisway == 2009 || countvariablethatalsoneedstobethisway == 17) {
                break
                Atleast1iteratedarraywithaccessedandusedelementsinit[Atleast1iteratedarraywithaccessedandusedelementsinit.length] = countvariablethatalsoneedstobethisway;
            }
            else {
                Atleast1iteratedarraywithaccessedandusedelementsinit[Atleast1iteratedarraywithaccessedandusedelementsinit.length] = countvariablethatalsoneedstobethisway;
            }
            countvariablethatalsoneedstobethisway++;
        }
        redundant("Data extraction complete; the following state id's have been purged: " + Atleast1iteratedarraywithaccessedandusedelementsinit, "warn");
    }
    else {
        trying++;
        if (trying < 11) {
            redundant("Failed press", "error");
        }
        else {
            const attacks = ["Stop it.", "Quit trying.", "You've tried " + trying + " times.", "Don't you think it's enough?", "Why do you still try?", "Are you listening to me?", "Quit it.", "What if there's a reason this isn't working?", "This isn't working.", "Denied.", "Denied!", "..."];
            redundant(attacks[trying % attacks.length], "error");
        }
    }
 }