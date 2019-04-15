## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. -->
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. -->
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' -->

## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## story_name
* give_name{"name":"Sam"}
 - utter_greet


## story_joke_01
* joke
 - action_send_token

## story_joke_02
* greet
 - utter_name
* give_name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' -->
 - utter_greet
* joke
 - action_send_token
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_login_01
* login
  - action_write_log
  - utter_ask_for_name
* give_name{"name":"Ayorkor", "last_name":"Brown-Pobee"}
  - action_write_log
  - action_send_token
  - utter_useful
* affirm
  - action_write_log
  - utter_thanks

## story_login_02
  * login
    - action_write_log
    - utter_ask_for_name
  * give_name{"name":"Ayorkor", "last_name":"Brown-Pobee"}
    - action_write_log
    - action_send_token
    - utter_useful
  * deny
    - action_write_log
    - utter_refer_to_person
    - action_send_email

## story_enroll_01
* enrollment
  - utter_ask_for_name
* give_name{"name":"Ayorkor", "last_name":"Brown-Pobee"}
  - utter_ask_for_course
* give_course{"course_name":"Literature in French"}
  - action_enrol_student

## story_list_courses_01
* list_course
  -action_list_all_courses

## story_send_manual
* navigation
  -action_send_manual

##story_greet
* greet
  - utter_name
* give_name{"name": "Dennis", "last_name":"Owusu"}
  - utter_full_name

##story_introduction
* introduction
  - utter_introduction_response

##story_age
* age
  - utter_age_response

##story_beautiful
* beautiful
  - utter_beautiful_response

##story_beautiful
* birthday
  - utter_birthday_response

##story_boss
* boss
  - utter_boss_response

##story_help
* help
  - utter_help_response

##story_help
* good
  - utter_good_response

##story_hobby
* hobby
  - utter_hobby_response
