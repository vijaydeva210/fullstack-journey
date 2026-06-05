document.querySelector('.buttons').addEventListener('click',values);
let previous_input='',value_before='',value_after='',operator='';
function values(event){
    let current_input,operator_keys,control_key,control_keys,output;
    operator_keys=['+','-','*','/']
    control_keys=['=','AC','C']
    current_input=event.target.innerText;    
    //--------------------------------------------------------> = C AC  controls handling
    if(control_keys.includes(current_input)){
        control_key=String(current_input);
        if (control_key=='='){
            value_after=Number(previous_input);
            if(operator == '+'){
                output=value_before+value_after;
            }else if(operator == '-'){
                output=value_before-value_after;
            }else if(operator == '*'){
                output=value_before*value_after;
            }else if(operator == '/'){
                output=value_before/value_after
            }
            document.querySelector('#display_text').value=output
            value_before='';
            value_after='';
            operator='';
            previous_input='';
        }else if(control_key == 'AC'){
            value_before='';
            value_after='';
            previous_input='';
            operator='';
            output='';
            document.querySelector('#display_text').value=output;
            
        }if(control_key == 'C'){
            console.log('current_input :',operator);
            if(operator_keys.includes(operator)){
                operator='';
                previous_input=value_before;
                document.querySelector('#display_text').value=previous_input;
            }else{
                previous_input=previous_input.slice(0,(previous_input.length)-1);
                document.querySelector('#display_text').value=previous_input;
            }

            console.log(previous_input,value_before);
        }
        
    }
    //-----------------------------------------------------------------------------> + - * / operators handling  
    else if(operator_keys.includes(current_input)){
        value_before=Number(previous_input);
        previous_input='';
        operator=current_input;
        document.querySelector('#display_text').value=operator;
    }
    //------------------------------------------------------------------------------> Adding numbers before operator and after operator
    else{
        if(current_input.length==1)previous_input=previous_input+current_input
        if(previous_input.length>0){
            document.querySelector('#display_text').value=previous_input;   
        }
    }
    console.log('previous_input:',previous_input)
    //console.log('value_before :',value_before,'value_after :',value_after)
    //console.log('output = ',output)
}