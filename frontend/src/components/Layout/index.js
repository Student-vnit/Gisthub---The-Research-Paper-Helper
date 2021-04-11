import React,{useState,useEffect} from 'react';
import GetAudio from '../getAudio';
import GetSummary from '../getSummary';
import GetText from '../getText';
import {fileuploadurl, getaudiourl} from '../urls';


function Layout(){

    const [pdfpath , setPdfpath] = useState(null)
    const [bytedata , setBytedata] = useState(null)
    const [pdffile , setPdffile] = useState(null)


    const handleSubmit = async (e) => {
        e.preventDefault()

        // const formdata = new FormData();

        // formdata.append('byteFile' , pdffile )
        // formdata.append('filename' , pdffile.name)



        console.log("filefile => " , pdffile)
        console.log("bytedata => " , bytedata)
        console.log('here1')


        
        // const data = await fetch('https://gisthub-vnit.herokuapp.com/pdf_initialize' , {
        //     method : 'POST',
        //     body : formdata
        // })


        var myHeaders = new Headers();
        myHeaders.append("byteFile", "");

        var formdata = new FormData();
        formdata.append("byteFile", pdffile);

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: formdata,
            redirect: 'follow'
        };

        fetch(fileuploadurl, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));



        console.log('here2')

       


        // await fetch('https://gisthub-vnit.herokuapp.com/pdf_initialize', {
        //         let data = new FormData()
        //         data.append('byteFile', e.target.files[0])

        //         method: 'POST',
        //         // headers: {
        //         //   'Content-Type': 'multipart/form-data'
        //         // },
        //         body: data
        //     })



        // console.log(pdffile)
        
    }

    const handleFileInput = e =>{
        const file=e.target.files[0]

        console.log(file)
        setPdffile(file)

     


        var reader = new FileReader();
        var fileByteArray = [];
        reader.readAsArrayBuffer(file);
        reader.onloadend = function (evt) {
            if (evt.target.readyState == FileReader.DONE) {
            var arrayBuffer = evt.target.result,
                array = new Uint8Array(arrayBuffer);
            for (var i = 0; i < array.length; i++) {
                fileByteArray.push(array[i]);
                }
            }
        }
        
        setBytedata(fileByteArray)
        console.log(fileByteArray)


    }

    useEffect(()=>{
        // console.log("saving pdffile name" , pdffile)
        if(pdffile)
        localStorage.setItem('pdffilename' , JSON.stringify(pdffile.name));
    },[pdffile])






    return(
        <div >

            {/* <div className="row" style={{backgroundColor:'gray',fontSize:20,padding:5,marginBottom:10}}>   
                <div className="col-2">
                    Logo
                </div>
                <div className="col-10">
                    Upload | Link to text part | summary | Audio
                </div>
            </div> */}


        <nav class="navbar navbar-expand-lg navbar-light bg-dark">
            <a class="navbar-brand" href="#"><img style={{height:60,width:60}} src={process.env.PUBLIC_URL + '/logo.jpeg'}/></a>
            <div style={{fontSize:35,color:'white'}}>
                GistHub
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav" >
                <ul class="navbar-nav ml-auto">
                <li class="nav-item active ">
                    <a class="nav-link" href="#" style={{color:'white',fontSize:25}}>Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" style={{color:'white',fontSize:25}}>Features</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" style={{color:'white',fontSize:25}}>Pricing</a>
                </li>
                </ul>
            </div>
            </nav>


        <div style={{margin:15,padding:10}}>
            <div className="container" >
                
                
            <div className="row jumbotron" style={{backgroundColor :'#ff8c00',textAlign:'center'}}>
                <div className="row" style={{textAlign:'center',margin:'auto'}}>
                    <form onSubmit={(e)=>handleSubmit(e)} style={{display:'flex' , flexDirection:'row'}}>
                        <div className="input-group mb-3" style={{margin:10}}>
                         <input className="form-control" type="file" onChange={handleFileInput} />
                        </div>
                        <button className="btn btn-dark"type="submit" style={{margin:10,height:45}}>Upload</button>
                    </form>
                </div>
            </div>



                <GetText pdffile={pdffile}/>



                <GetSummary pdffile={pdffile}/>
                
                
                
                <GetAudio pdffile={pdffile}/>
                
            </div>
        </div>



            <footer class="page-footer font-small blue" style={{backgroundColor:'#343a40',paddingTop:15}}>
                <div className="row">
                <div className="col" style={{color:'white'}}>
                    About Us
                </div>
                <div className="col" style={{color:'white'}}>
                    Contact Us
                </div>
                </div>
                <div class="footer-copyright text-center py-3" style={{color:'white'}}>© 2020 Copyright:
                    <a href="https://mdbootstrap.com/"> GistHub</a>
                </div>

            </footer>


            

        </div>

    )
}


export default Layout;