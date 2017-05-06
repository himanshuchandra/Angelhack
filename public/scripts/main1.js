// Grab elements, create settings, etc.
var video;
var canvas;
var context;
var snap;
var myImage
var timer;
var val;
var dataURL;
var url;
window.addEventListener("load",function(){
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    context = canvas.getContext('2d');
    
//    context.dropshadow = '(5px,5px,5px,red)';
//    context.filter='contrast(100px)';
//    context.filter='invert(100%)';
    snap = document.getElementById('snap');
    snap.addEventListener("click", function() {
//        val=parseInt(document.getElementById('outputID').value);
        timer = setInterval(function(){
       val=parseInt(document.getElementById('outputID').value);
       
    },1000);
        context.filter = 'grayscale('+val+'%)';
        
//        dataURL = canvas.toDataURL();
         myImage = canvas.toDataURL("image/jpeg");
        //   if(myImage!=undefined){
//          alert(myImage.replace(/^data:image\/(png|jpg);base64,/, ""));
//          }
// //            document.write('<img src="'+myImage+'"/>');
//        window.location.href=myImage;
        context.drawImage(video, 0, 0, 640, 480);
         var imgData = context.getImageData(0, 0, 640, 480);
         console.log(imgData);
        //  document.getElementById("c").getContext("2d").putImageData(imgData,220, 100, 220, 100,400,300);
        create1();
    //     context.font = '48px serif';
    // context.strokeText('Hello world', 50, 100);
});
// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.src = window.URL.createObjectURL(stream);
        video.play();
    });
}

});


function create1(){
    var link = document.createElement("a");

//     // var img=document.getElementById("img");
//     if(document.getElementById("img")==null){
//     img = document.createElement("img");
//     img.setAttribute("id","img");
// }
    link.href=canvas.toDataURL();
    link.download="img.jpeg";
    link.innerHTML="click";
//    img.height=200;
    document.getElementById("div1").appendChild(link);
}

 function to_image(){
//                var canvas = document.getElementById("thecanvas");
                document.getElementById("img").src = myImage;
                Canvas2Image.saveAsPNG(canvas);
            }



