from main_window import MainWindow
import cmd_examples as ce

main_window = None

if __name__ == '__main__':
    main_window = MainWindow(resize=True, title='Commander', cmdlist=ce.cmdlist, bgcolor='#4b4b4b', fgcolor='#98fb98')

    main_window.run()