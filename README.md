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
> Note: If you will omit 'name' attribute then the text filed input will not be submitted to server.

### HTML textarea tag in form
* The <textarea> tag in HTML is used to insert multiple-line text in a form. The size of <textarea> can be specify either using "rows" or "cols" attribute or by CSS.

### Example:
 ~~~ Html
 <form>  
        Enter your address:<br>  
      <textarea rows="2" cols="20"></textarea>  
  </form> 
 ~~~
 ![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-textarea-tag-in-form.png)]
 
### Label Tag in Form
* It is considered better to have label in form. As it makes the code parser/browser/user friendly.
* If you click on the label tag, it will focus on the text control. To do so, you need to have for attribute in label tag that must be same as id attribute of input tag.

> NOTE: It is good to use <label> tag with form, although it is optional but if you will use it, then it will provide a focus when you tap or click on label tag. It is more worthy with touchscreens.

~~~ Html
<form>  
    <label for="firstname">First Name: </label> <br/>  
              <input type="text" id="firstname" name="firstname"/> <br/>  
   <label for="lastname">Last Name: </label>  
              <input type="text" id="lastname" name="lastname"/> <br/>  
 </form>  
~~~
![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-label-tag-in-form.png)]

### HTML Password Field Control
* The password is not visible to the user in password field control.
### Example
~~~ Html
<form>  
    <label for="password">Password: </label>  
              <input type="password" id="password" name="password"/> <br/>  
</form>  
~~~
![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-password-field-control.png)]

### HTML Email Field Control
* The email field in new in HTML 5. It validates the text for correct email address. You must use @ and . in this field.
~~~ Html
<form>  
    <label for="email">Email: </label>  
              <input type="email" id="email" name="email"/> <br/>  
</form>  
~~~
![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-5-email-field-control.png)]

> Note: If we will not enter the correct email, it will display error like:
![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-5-email-field-control2.png)]

### Radio Button Control
* The radio button is used to select one option from multiple options. It is used for selection of gender, quiz questions etc.

* If you use one name for all the radio buttons, only one radio button can be selected at a time.

* Using radio buttons for multiple options, you can only choose a single option at a time.

~~~ Html
<form>  
    <label for="gender">Gender: </label>  
              <input type="radio" id="gender" name="gender" value="male"/>Male  
              <input type="radio" id="gender" name="gender" value="female"/>Female <br/>  
</form>  
~~~


![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/radio-button-control.png)]

### Checkbox Control
* The checkbox control is used to check multiple options from given checkboxes.
~~~ Html
<form>  
Hobby:<br>  
              <input type="checkbox" id="cricket" name="cricket" value="cricket"/>  
                 <label for="cricket">Cricket</label> <br>  
              <input type="checkbox" id="football" name="football" value="football"/>  
                 <label for="football">Football</label> <br>  
              <input type="checkbox" id="hockey" name="hockey" value="hockey"/>  
                 <label for="hockey">Hockey</label>  
</form>  
~~~
> Note: These are similar to radio button except it can choose multiple options at a time and radio button can select one button at a time, and its display.

![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/checkbox-control.png)]

### Submit button control
* HTML <input type="submit"> are used to add a submit button on web page. When user clicks on submit button, then form get submit to the server.
### Syntax:
~~~ Html
<input type="submit" value="submit">  
~~~
* The type = submit , specifying that it is a submit button

* The value attribute can be anything which we write on button on web page.

* The name attribute can be omit here.
### Example
~~~ Html
<form>  
    <label for="name">Enter name</label><br>  
    <input type="text" id="name" name="name"><br>  
    <label for="pass">Enter Password</label><br>  
    <input type="Password" id="pass" name="pass"><br>  
    <input type="submit" value="submit">  
</form>  
~~~

![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/submit-button-control.png)]

### HTML <fieldset> element:
 * The <fieldset> element in HTML is used to group the related information of a form. This element is used with <legend> element which provide caption for the grouped elements.
### Example
 ~~~ Html
 <form>  
     <fieldset>  
      <legend>User Information:</legend>  
    <label for="name">Enter name</label><br>  
<input type="text" id="name" name="name"><br>  
<label for="pass">Enter Password</label><br>  
<input type="Password" id="pass" name="pass"><br>  
<input type="submit" value="submit">  
</fieldset>  
</form>  
 ~~~


![IMAGE ALT TEXT HERE](https://static.javatpoint.com/htmlpages/images/html-fieldset-element.png)


### Forms with Bootstrap 4

### Bootstrap Form Layouts
 * Bootstrap provides three types of form layouts:
   * Vertical form (this is default)
   * Horizontal form
   * Inline form

* Standard rules for all three form layouts
  * Wrap labels and form controls in &lt;div class="form-group"&gt; (needed for optimum spacing)
  * Add class .form-control to all textual &lt;input&gt;, &lt;textarea&gt;, and &lt;select&gt; element
### Bootstrap Vertical Form (default)
 * The following example creates a vertical form with two input fields, one checkbox, and a submit button:

~~~ Html
<form action="#">
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <div class="checkbox">
    <label><input type="checkbox"> Remember me</label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
~~~
![IMAGE ALT TEXT HERE](https://github.com/vijaykumar10022/data/blob/master/vertical%20form.JPG)
### Bootstrap Inline Form
* In an inline form, all of the elements are inline, left-aligned, and the labels are alongside.
> Note: This only applies to forms within viewports that are at least 768px wide!
* Additional rule for an inline form:
* Add class .form-inline to the &lt;form&gt; element
~~~ Html
<form class="form-inline" action="#">
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <div class="checkbox">
    <label><input type="checkbox"> Remember me</label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
~~~
![IMAGE ALT TEXT HERE](https://github.com/vijaykumar10022/data/blob/master/inline%20form.JPG)

### Bootstrap Horizontal Form
* A horizontal form means that the labels are aligned next to the input field (horizontal) on large and medium screens. On small screens (767px and below), it will transform to a vertical form (labels are placed on top of each input).
* Additional rules for a horizontal form:
 * Add class .form-horizontal to the &lt;form&gt; element
Add class .control-label to all &lt;label&gt; elements
> Tip: Use Bootstrap's predefined grid classes to align labels and groups of form controls in a horizontal layout
~~~ Html
<form class="form-horizontal" action="/action_page.php">
  <div class="form-group">
    <label class="control-label col-sm-2" for="email">Email:</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="email" placeholder="Enter email">
    </div>
  </div>
  <div class="form-group">
    <label class="control-label col-sm-2" for="pwd">Password:</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="pwd" placeholder="Enter password">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <div class="checkbox">
        <label><input type="checkbox"> Remember me</label>
      </div>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-default">Submit</button>
    </div>
  </div>
</form>
~~~
![IMAGE ALT TEXT HERE](https://github.com/vijaykumar10022/data/blob/master/Horizontal%20form.JPG)
------
### Bootstrap Form Inputs
 * Supported Form Controls
  * input
  * textarea
  * checkbox
  * radio
  * select
### Bootstrap Input
* Bootstrap supports all the HTML5 input types: text, password, datetime, datetime-local, date, month, time, week, number, email, url, search, tel, and color.
> Note: Inputs will NOT be fully styled if their type is not properly declared!
### Example
~~~ Html
<div class="form-group">
  <label for="usr">Name:</label>
  <input type="text" class="form-control" id="usr">
</div>
<div class="form-group">
  <label for="pwd">Password:</label>
  <input type="password" class="form-control" id="pwd">
</div>
~~~

### Bootstrap Textarea
### Example
~~~ Html
<div class="form-group">
  <label for="comment">Comment:</label>
  <textarea class="form-control" rows="5" id="comment"></textarea>
</div>
~~~

### Bootstrap Checkboxes
* Checkboxes are used if you want the user to select any number of options from a list of preset options.
### Example
~~~ Html
<div class="checkbox">
  <label><input type="checkbox" value="">Option 1</label>
</div>
<div class="checkbox">
  <label><input type="checkbox" value="">Option 2</label>
</div>
<div class="checkbox disabled">
  <label><input type="checkbox" value="" disabled>Option 3</label>
</div>
~~~
> Use the .checkbox-inline class if you want the checkboxes to appear on the same line:
### Bootstrap Radio Buttons
* Radio buttons are used if you want to limit the user to just one selection from a list of preset options.
### Example
~~~ Html
<div class="radio">
  <label><input type="radio" name="optradio" checked>Option 1</label>
</div>
<div class="radio">
  <label><input type="radio" name="optradio">Option 2</label>
</div>
<div class="radio disabled">
  <label><input type="radio" name="optradio" disabled>Option 3</label>
</div>
~~~
> Use the .radio-inline class if you want the radio buttons to appear on the same line:
### Bootstrap Select List
* Select lists are used if you want to allow the user to pick from multiple options.
~~~ Html
<div class="form-group">
  <label for="sel1">Select list:</label>
  <select class="form-control" id="sel1">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
  </select>
</div>
~~~
### Basic Media Object
* Bootstrap provides an easy way to align media objects (like images or videos) to the left or to the right of some content. This can be used to display blog comments, tweets and so on:
### Example
~~~ Html
<!-- Left-aligned -->
<div class="media">
  <div class="media-left">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">John Doe</h4>
    <p>Lorem ipsum...</p>
  </div>
</div>

<!-- Right-aligned -->
<div class="media">
  <div class="media-body">
    <h4 class="media-heading">John Doe</h4>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
  </div>
  <div class="media-right">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
</div>
~~~


#### Bootstrap Registeration Form
~~~ Html
<div class="container">
            <form class="form-horizontal" role="form">
                <h2>Registration</h2>
                <div class="form-group">
                    <label for="firstName" class="col-sm-3 control-label">First Name</label>
                    <div class="col-sm-8">
                        <input type="text" id="firstName" placeholder="First Name" class="form-control" autofocus>
                    </div>
                </div>
                <div class="form-group">
                    <label for="lastName" class="col-sm-3 control-label">Last Name</label>
                    <div class="col-sm-9">
                        <input type="text" id="lastName" placeholder="Last Name" class="form-control" autofocus>
                    </div>
                </div>
                <div class="form-group">
                    <label for="email" class="col-sm-3 control-label">Email* </label>
                    <div class="col-sm-9">
                        <input type="email" id="email" placeholder="Email" class="form-control" name= "email">
                    </div>
                </div>
                <div class="form-group">
                    <label for="password" class="col-sm-3 control-label">Password*</label>
                    <div class="col-sm-9">
                        <input type="password" id="password" placeholder="Password" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label for="password" class="col-sm-3 control-label">Confirm Password*</label>
                    <div class="col-sm-9">
                        <input type="password" id="password" placeholder="Password" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label for="birthDate" class="col-sm-3 control-label">Date of Birth*</label>
                    <div class="col-sm-9">
                        <input type="date" id="birthDate" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label for="phoneNumber" class="col-sm-3 control-label">Phone number </label>
                    <div class="col-sm-9">
                        <input type="phoneNumber" id="phoneNumber" placeholder="Phone number" class="form-control">
                        <span class="help-block">Your phone number won't be disclosed anywhere </span>
                    </div>
                </div>
                <div class="form-group">
                        <label for="Height" class="col-sm-3 control-label">Height* </label>
                    <div class="col-sm-9">
                        <input type="number" id="height" placeholder="Please write your height in centimetres" class="form-control">
                    </div>
                </div>
                 <div class="form-group">
                        <label for="weight" class="col-sm-3 control-label">Weight* </label>
                    <div class="col-sm-9">
                        <input type="number" id="weight" placeholder="Please write your weight in kilograms" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label class="control-label col-sm-3">Gender</label>
                    <div class="col-sm-6">
                        <div class="row">
                            <div class="col-sm-4">
                                <label class="radio-inline">
                                    <input type="radio" id="femaleRadio" value="Female">Female
                                </label>
                            </div>
                            <div class="col-sm-4">
                                <label class="radio-inline">
                                    <input type="radio" id="maleRadio" value="Male">Male
                                </label>
                            </div>
                        </div>
                    </div>
                </div> <!-- /.form-group -->
                <div class="form-group">
                    <div class="col-sm-9 col-sm-offset-3">
                        <span class="help-block">*Required fields</span>
                    </div>
                </div>
                <button type="submit" class="btn btn-primary btn-block">Register</button>
            </form> <!-- /form -->
        </div> <!-- ./container -->
~~~
![IMAGE ALT TEXT HERE](https://github.com/vijaykumar10022/data/blob/master/registration%20form.JPG)
