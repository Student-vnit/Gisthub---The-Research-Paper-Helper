import React, { useState  , useEffect} from 'react';
import {fileuploadurl, gettexturl} from '../urls'
import './scroll.css'

function GetText ({pdffile}) {

    // console.log("getText => ", pdffile)

    const [text , setText] = useState('');
    const [loading ,setLoading] = useState(false)

    const fetchText = () => {
        setLoading(true)

        var myHeaders = new Headers();
        myHeaders.append("byteFile", "");

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            redirect: 'follow'
          };

        let savedFileName = localStorage.getItem('pdffilename');
        

        let filename = (pdffile) ? pdffile.name : savedFileName.substring(1 , savedFileName.length-1);
      
        console.log(filename)

        fetch(`${gettexturl}?filename=${filename}`, requestOptions)
        .then(response => response.text())
        .then(result => {
            console.log(result)
            setText(result)
        })
        .catch(error => console.log('error', error));

        setLoading(false)

    }

    
   





    return(
        <div className="row jumbotron" style={{backgroundColor:'black'}}>
           
            {loading ? 
                <p>Loading...</p>
                :
                <div style={{display:'flex' ,flex:1,justifyContent:'center'}}>
                    {text.length === 0 ? 
                        <div >
                            <button onClick={()=>fetchText()} className="btn btn-info" style={{height:45, width:200}}>Get Extracted Text</button>
                        </div>
                        :
                        <div>
                            <p className="scrollbar scrollbar-primary mx-auto"
                            style={{color:'white',height:300,fontSize:15}}>{text}</p>
                        
                        </div>
                    }   
                </div>
            }
         
        </div>
        
    )
}

export default GetText;