## Form Handling using a basic procedure with bootstrap4. 

### What is The Form?
* Form (HTML) A webform, web form or HTML form on a web page allows a user to enter data that is sent to a server for processing. Forms can resemble paper or database forms because web users fill out the forms using checkboxes, radio buttons, or text fields.
### Where Forms are using?
* HTML Forms are required when you want to collect some data from the site visitor.
  * For example during user registration you would like to collect information such as name, email,address, credit card, etc.
* A form will take input from the site visitor and then will post it to a back-end application such as Django,Flask,CGI, ASP Script or PHP script etc.
* The back-end application will perform required processing on the passed data based on defined business logic inside the application.
### HTML Form Syntax
```Html
<form action="server url" method="get|post">  
  //input controls e.g. textfield, textarea, radiobutton, button  
</form> 
```
### HTML Form Tags
<table class="alt">
<tr><th>Tag</th><th>Description</th></tr>
<tr><td>&lt;form&gt;</td><td>It defines an HTML form to enter inputs by the used side.</td></tr>
<tr><td>&lt;input&gt;</td><td>It defines an input control.</td></tr>
<tr><td>&lt;textarea&gt;</td><td>It defines a multi-line input control.</td></tr>
<tr><td>&lt;label&gt;</td><td>It defines a label for an input element.</td></tr>
<tr><td>&lt;fieldset&gt;</td><td>It groups the related element in a form.</td></tr>
<tr><td>&lt;legend&gt;</td><td>It defines a caption for a &lt;fieldset&gt; element.</td></tr>
<tr><td>&lt;select&gt;</td><td>It defines a drop-down list.</td></tr>
<tr><td>&lt;optgroup&gt;</td><td>It defines a group of related options in a drop-down list.</td></tr>
<tr><td>&lt;option&gt;</td><td>It defines an option in a drop-down list.</td></tr>
<tr><td>&lt;button&gt;</td><td>It defines a clickable button.</td></tr>
</table>

### HTML &lt;form&gt; element
* The HTML <form> element provide a document section to take input from user. It provides various interactive controls for submitting information to web server such as text field, text area, password field, etc.

> Note: The <form> element does not itself create a form but it is container to contain all required form elements, such as <input>, <label>, etc.

### Syntax:
~~~ Html
<form>  
//Form elements  
</form>
~~~~

### HTML &lt;input&gt; element
  * The HTML <input> element is fundamental form element. It is used to create form fields, to take input from user. We can apply different input filed to gather different information form user. Following is the example to show the simple text input.
### Example
~~~ Html
<form>  
     Enter your name  <br>  
    <input type="text" name="username">  
  </form>
~~~
![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-form.png)]

### HTML TextField Control
* The type="text" attribute of input tag creates textfield control also known as single line textfield control. The name attribute is optional, but it is required for the server side component such as JSP, ASP, PHP etc.
### Example
~~~ Html
<form>  
    First Name: <input type="text" name="firstname"/> <br/>  
    Last Name:  <input type="text" name="lastname"/> <br/>  
 </form> 
~~~
![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-textfield-control.png)]

