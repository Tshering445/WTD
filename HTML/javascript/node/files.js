const fs = require('fs');


// read Files
const myFile = './docs/blog.txt';
// callback function
fs.readFile(myFile, (err,data)=>{
    if (err){
        console.log("An error occured: " + err);

    }else{
        console.log(data.toString());
    }
});

//Write into files
fs.writeFile(myFile, 'good day!', (err) => {
    if(err){
        console.log(err);
    
    }else{
        console.log("The file was updated");
    }
})

fs.appendFile(myFile, 'bye bye!', (err) => {
    if(err){
        console.log(err);
    
    }else{
        console.log("The file was updated");
    }
})


