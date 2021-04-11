import React, { useEffect, useState } from 'react';
import {fileuploadurl, getaudiourl} from '../urls';



function _base64ToArrayBuffer(base64) {
    var binary_string = window.atob(base64);
    var len = binary_string.length;
    var bytes = new Uint8Array(len);
    for (var i = 0; i < len; i++) {
        bytes[i] = binary_string.charCodeAt(i);
    }
    return bytes.buffer;
}


function useForceUpdate(){
    const [value, setValue] = useState(0); // integer state
    return () => setValue(value => value + 1); // update the state to force render
}



function GetAudio ({pdffile}) {


    const [byteAudioData , setByteAudioData] = useState(null)
    const [got  , setGot] = useState(false);
    const [stateChanger , setStateChanger] = useState(0);
    const [interval , setIterval] = useState(null)

    const [fileName ,setFileName] = useState((pdffile) ? pdffile.name : '')

    const fetchaudio = () => {

        console.log(fileName)

        console.log(pdffile)

        setStateChanger(stateChanger +1);
    }

    const forceUpdate = useForceUpdate();

    // useEffect(()=>{
    //     function setfunction(){
    //         let savedFileName = localStorage.getItem('pdffilename');
            

    //         let filename = '';
    //         if(savedFileName){
    //             filename = savedFileName.substring(1 , savedFileName.length-1);
    //         }
    //         if(pdffile){
    //             filename = pdffile.name;
    //         }

    //         setFileName(filename)
    //     }
    //     setfunction();
    // },[])




    return(

        <div className="row jumbotron" style={{padding:20,backgroundColor:'black'}}>
            <div style={{display:'flex' , flex:1 , justifyContent:'center'}}>
                
                <audio controls>
             
                {pdffile?
                <div>
                <source src={'https://gisthub-softlab.herokuapp.com/get_mp3?filename='+ pdffile.name  } type="audio/ogg"/>
                </div>
                    :
                    <div>
                <source src={'https://gisthub-softlab.herokuapp.com/get_mp3?filename='+ "yolo.pdf"  } type="audio/ogg"/>
                </div>

                }

              
                {/* <source src="horse.mp3" type="audio/mpeg"/> */}
                Your browser does not support the audio element.
                </audio>
                <button style={{marginTop : 10,margin:5}}class="btn btn-info" onClick={forceUpdate}><span class="glyphicon glyphicon-refresh"></span>Refresh</button>
            </div>

        </div>
    )
}

export default GetAudio;