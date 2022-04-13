// animation text


const txtAnim = document.querySelector('.txt-animation');

let typewriter = new Typewriter(txtAnim, {
  loop: false,
  deleteSpeed: 20
})

typewriter
.pauseFor(1800)
.changeDelay(20)
.typeString('Bienvenue dans le groupe HYPNOS. Découvrez nos hôtels: ')
.pauseFor(300)
.typeString('<strong>, Le Cocooning <strong>')
.pauseFor(1000)
.deleteChars(12)
.typeString('<span style="color: #27ae60;">, Le Kilimandjaro <span>')

.start()