// animation text

const txtAnim = document.querySelector('.txt-animation');

let typewriter = new Typewriter(txtAnim, {
  loop: false,
  deleteSpeed: 20
});

typewriter
.pauseFor(1000)
.changeDelay(50)
.typeString('Bienvenue chez Hypnos<br/>' )
.pauseFor(300)
.typeString('<span style="color: #01a3a4;"><strong> Le Cocooning </strong>')
.pauseFor(1200)
.deleteChars(13)
.typeString('<span style="color: #27ae60;"><strong> Le Kilimandjaro </strong></span>')
.pauseFor(1200)
.deleteChars(16)
.typeString('<span style="color: #fff200;"><strong><strong> Le Splendid Hotel </strong></span>')
.pauseFor(1200)
.deleteChars(18)
.typeString('<span style="color: #576574;"><strong> Le Carlton </strong></span>')
.pauseFor(1200)
.deleteChars(11)
.typeString('<span style="color: #3dc1d3;"><strong> Le Beach Hotel </strong></span>')
.pauseFor(1200)
.deleteChars(15)
.typeString('<span style="color: #5f27cd;"><strong> Casino Royale </strong></span>')
.pauseFor(1200)
.deleteChars(14)
.typeString('<span style="color: #7efff5;"><strong> Hotel Meetic </strong></span>')
.pauseFor(1200)
.deleteChars(13)

.start();