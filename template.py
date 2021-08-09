def template_test_class():
    return '''/**
* @author {author}
*/
@isTest
private class {class_name}Test {{
{class_body}
}}
'''

def template_test_method():
    return '''
    /**
     * This is a test method for {function_name}
     */
    static testMethod void test_{function_name}() {{

        // PageReference pageRef = Page.{page_name};
        // Test.setCurrentPage(pageRef);
        // pageRef.getParameters().put('param1', 'param1');

        Test.startTest();

{function_body}

        Test.stopTest();

        // Check
        // System.assert(ApexPages.hasMessages());
        // for(ApexPages.Message msg : ApexPages.getMessages()) {{
        //     System.assertEquals('Upload file is NULL', msg.getSummary());
        //     System.assertEquals(ApexPages.Severity.ERROR, msg.getSeverity());
        // }}
    }}

'''



def template_class():
    return '''/**
* @author {author}
*/
public with sharing class {class_name}{class_type} {{
         public {class_name}{class_type}() {{

         }}
{class_body}
}}
'''