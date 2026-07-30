// ======================================
// ELEMENTOS
// ======================================

const filtroPais = document.getElementById("filtroPais");
const orden = document.getElementById("orden");
const direccion = document.getElementById("direccion");

const tbody = document.querySelector("#tabla tbody");

const contador = document.getElementById("contador");

// ======================================
// CONVERTIR TEXTO A NÚMERO
// ======================================

function convertirUsuarios(valor){

    valor = valor.replace("B","000").replace("M","");

    return parseFloat(valor);

}

// ======================================
// ORDENAR TABLA
// ======================================

function ordenar(){

    const filas = [...tbody.querySelectorAll("tr")];

    const tipo = orden.value;

    const dir = direccion.value;

    filas.sort((a,b)=>{

        let A;
        let B;

        switch(tipo){

            case "nombre":

                A = a.cells[0].innerText.trim().toLowerCase();
                B = b.cells[0].innerText.trim().toLowerCase();

                break;

            case "usuarios":

                A = convertirUsuarios(a.cells[1].innerText);

                B = convertirUsuarios(b.cells[1].innerText);

                break;

            case "fundado":

                A = Number(a.cells[2].innerText);

                B = Number(b.cells[2].innerText);

                break;

            case "pais":

                A = a.cells[3].innerText.trim();

                B = b.cells[3].innerText.trim();

                break;

        }

        if(A<B){

            return dir=="asc" ? -1 : 1;

        }

        if(A>B){

            return dir=="asc" ? 1 : -1;

        }

        return 0;

    });

    filas.forEach(f=>tbody.appendChild(f));

}

// ======================================
// FILTRAR
// ======================================

function filtrar(){

    let visibles = 0;

    document.querySelectorAll("#tabla tbody tr").forEach(fila=>{

        const pais = fila.dataset.pais;

        if(filtroPais.value=="Todos" || pais==filtroPais.value){

            fila.style.display="";

            visibles++;

        }

        else{

            fila.style.display="none";

        }

    });

    contador.innerText = visibles;

}

// ======================================
// EVENTOS
// ======================================

filtroPais.addEventListener("change",()=>{

    filtrar();

});

orden.addEventListener("change",()=>{

    ordenar();

});

direccion.addEventListener("change",()=>{

    ordenar();

});

// ======================================
// EFECTO HOVER
// ======================================

document.querySelectorAll(".btn-detalle").forEach(btn=>{

    btn.addEventListener("mouseenter",()=>{

        btn.style.transform="scale(1.08)";

    });

    btn.addEventListener("mouseleave",()=>{

        btn.style.transform="scale(1)";

    });

});

// ======================================
// CARGA
// ======================================

window.onload=()=>{

    ordenar();

    filtrar();

}