#!/usr/bin/env python
import os
import sys
import openai
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wxcloudrun.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    StartRobot()

def StartRobot():
    import werobot
    robot = werobot.WeRoBot(token='tokenhere')

    @robot.handler
    def response_message(message):
        user_input = message.content
        response = generate_response(user_input)
        return response


    # 让服务器监听在 0.0.0.0:80
    robot.config['HOST'] = '0.0.0.0'
    robot.config['PORT'] = 80
    robot.run()

if __name__ == '__main__':
    main()
