/* jshint esversion: 6 */


function main() { // wrapper function
    /**
     * Navbar functions
     *
     *
     */
    function navbar_open() {
        document.getElementById("nav-side-bar").style.display = "block";
    }

    function navbar_close() {
        document.getElementById("nav-side-bar").style.display = "none";
    }

    document.getElementById("nav-open-side-bar").addEventListener('click', ()=> {
        navbar_open();
    });
    document.getElementById("nav-close-side-bar").addEventListener('click', ()=> {
        navbar_close();
    });

    /**
     * Other content
     */

}// main

main();

