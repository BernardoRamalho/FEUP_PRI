
let ratingStart = document.querySelector('#ratingStart')
let ratingEnd = document.querySelector('#ratingEnd')
if (ratingStart && ratingEnd){
    ratingStart.addEventListener("change", function(event){
        
        let startValue = ratingStart.value;
        let endValue = ratingEnd.value;

        if (startValue > endValue){
            ratingEnd.value = startValue;
        }
        
    });

    ratingEnd.addEventListener("change", function(event){
        let startValue = ratingStart.value;
        let endValue = ratingEnd.value;

        if (endValue < startValue){
            ratingStart.value = endValue;
        }
    });
}


let pagesStart = document.querySelector('#pagesStart')
let pagesEnd = document.querySelector('#pagesEnd')
if (pagesStart && pagesEnd){
    pagesStart.addEventListener("change", function(event){
        
        let startValue = pagesStart.value;
        let endValue = pagesEnd.value;

        if (startValue > endValue){
            pagesEnd.value = startValue;
        }
        
    });

    pagesEnd.addEventListener("change", function(event){
        let startValue = pagesStart.value;
        let endValue = pagesEnd.value;

        if (endValue < startValue){
            pagesStart.value = endValue;
        }
    });
}


let reviewsStart = document.querySelector('#reviewsStart')
let reviewsEnd = document.querySelector('#reviewsEnd')
if (reviewsStart && reviewsEnd){
    reviewsStart.addEventListener("change", function(event){
        
        let startValue = reviewsStart.value;
        let endValue = reviewsEnd.value;

        if (startValue > endValue){
            reviewsEnd.value = startValue;
        }
        
    });

    reviewsEnd.addEventListener("change", function(event){
        let startValue = reviewsStart.value;
        let endValue = reviewsEnd.value;

        if (endValue < startValue){
            reviewsStart.value = endValue;
        }
    });
}

let totalratingsStart = document.querySelector('#totalratingsStart')
let totalratingsEnd = document.querySelector('#totalratingsEnd')
if (totalratingsStart && totalratingsEnd){
    totalratingsStart.addEventListener("change", function(event){
        
        let startValue = totalratingsStart.value;
        let endValue = totalratingsEnd.value;

        if (startValue > endValue){
            totalratingsEnd.value = startValue;
        }
        
    });

    totalratingsEnd.addEventListener("change", function(event){
        let startValue = totalratingsStart.value;
        let endValue = totalratingsEnd.value;

        if (endValue < startValue){
            totalratingsStart.value = endValue;
        }
    });
}
