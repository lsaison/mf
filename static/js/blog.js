// import EditorJS from 'npm/@editorjs/editorjs@latest';
// import Header from '@editorjs/header';

  const editor = new EditorJS({
  /**
   * Id of Element that should contain the Editor
   */
   holder : 'editorjs',

   /**
    * Available Tools list.
    * Pass Tool's class or Settings object for each Tool you want to use
    */
   tools: {
     header: {
       class: Header,
       inlineToolbar : true,
     },
     delimiter:Delimiter,
     paragraph:{
       class: Paragraph,
       inlineToolbar : true,
     },
     embed: Embed,
     image: SimpleImage,
     // ...
   },
 
   /**
    * Previously saved data that should be rendered
    */
   data: {}
  });

  function myFunction(){
    editor.save().then((output) =>{
      console.log('Data: ', output);
    }).catch((error) => {
      console.log('Saving failed : ', error)
    });
    }