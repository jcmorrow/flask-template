from app import create_app, Widget

app = create_app()


class SampleScript:
    @staticmethod
    def run():
        for widget in Widget.query.all():
            print(widget)


if __name__ == '__main__':
    with app.app_context():
        SampleScript.run()
