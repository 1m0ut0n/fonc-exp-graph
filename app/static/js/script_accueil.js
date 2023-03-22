window.addEventListener(
    "scroll",
    () => {
      document.body.style.setProperty(
        "--scroll",
        window.pageYOffset / (document.body.offsetHeight - window.innerHeight)
      );
    },
    false
  );


document.querySelector('h1').addEventListener('click', function() {
  alert("pourquoi tu cliques fdp ?????");
  })


  const observer = new IntersectionObserver(entries => {
    entries.forEach((entry) => {
      console.log(entry)
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
      }else{
        entry.target.classList.remove('show');
      }
    });
  });

  const hiddenElements = document.querySelectorAll('hidden'); 
  hiddenElements.forEach((el)=>observer.observe(el));
  
  /*activer bouton à scroll =1.3*/
