var count=0;
function start(){
    var r = document.getElementById("result");
if("webkitSpeechRecognition" in window){
    var speechRecognizer = new webkitSpeechRecognition();
    speechRecognizer.continuous = true;
    speechRecognizer.interimResults = true;
    speechRecognizer.lang = "en-IN";
    speechRecognizer.start();
    
    var finalTranscripts = "";
    speechRecognizer.onresult = function(event){
        var interimTranscripts = "";
        
       
        // startRecording(this);
        for(var i=event.resultIndex; i<event.results.length; i++){
            
            var transcript = event.results[i][0].transcript;
            transcript.replace("\n", "<br>");
            if(event.results[i].isFinal){
                finalTranscripts += transcript;
                
                count = (temp.match(/is/g) || []).length + s.length - s.replace(/Dun/g, "").length ;

                if(count>=3){
                    document.getElementById('done').submit();
                }
                // if(finalTranscripts.count("Done")+finalTranscripts.count("Dun")>=3){
                //     document.getElementById('done').submit();
                // }
                // if(finalTranscripts.includes("done") || finalTranscripts.includes("dun") )
                // {
                    
                //     count++;
                //     console.log(count);
                //     if(count>=3){
                //         // action="/"
                //         document.getElementById('done').submit();
                //     }
                //     // stopRecording(this);
                //     // startRecording(this);
                // }
                // else{
                //     // stopRecording(this);
                //     // startRecording(this);
                // }

            }
            else{
                interimTranscripts += transcript;
                // stopRecording(this);
                // startRecording(this);
            }
            r.innerHTML = finalTranscripts + '<span style="color: #999;">' + interimTranscripts + '</span>';
        }
    };
    speechRecognizer.onerror = function(event){
    };
}
else{
    r.innerHTML = "Your browser does not support that.";
}
}