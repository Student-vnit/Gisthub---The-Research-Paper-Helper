import React, { useState } from 'react'
import {getsummaryurl} from '../urls'


function GetSummary ({pdffile}) {


    const [summary , setSummary] = useState('')
    const [loading, setLoading] = useState(false)


    const fetchsummary = () => {
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

        fetch(`${getsummaryurl}?filename=${filename}`, requestOptions)
        .then(response => response.text())
        .then(result => {
            console.log(result)
            setSummary(result)
        })
        .catch(error => console.log('error', error));
        setLoading(false)
    }


    return(
        
        <div className="row jumbotron" style={{backgroundColor:'#ff8c00'}}>
           
            {loading ? 
                <p>Loading...</p>
                :
                <div style={{display:'flex' ,flex:1,justifyContent:'center'}}>
                    {summary.length === 0 ? 
                        <div >
                            <button onClick={()=>fetchsummary()} className="btn btn-info" style={{height:45, width:200}}>Get Text Summary</button>
                        </div>
                        :
                        <div>
                            <p className="scrollbar scrollbar-primary mx-auto"
                            style={{color:'black',height:300,fontSize:20}}>{summary.replace(/<[^>]+>/g, '')}</p>
                        
                        </div>
                    }   
                </div>
            }
         
        </div>
    )
}

export default GetSummary