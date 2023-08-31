

# detection event
def detection(self):
    exit = False
    # check what options are enabled
    for value in self.detectionReaction:
       if value.lower() == "exit":
           exit = True

    # check if exit event is enabled
    if exit == True:
        """ exit event is enabled: """
        # get pid
        import os
        pid = os.getpid()
        # close process by pid
        import signal
        os.kill(pid, signal.SIGINT)


# run all selected checks
def checks(self):
    import time
    while True:
        # config loop timeout
        time.sleep(int(self.loop_timeout))

        # check if anti debug is enabled
        if self.anti_debug == True:
            from debugCheck import debugChecks_main
            # run anti debug checks and return results
            if debugChecks_main(self):
                # debugger detected
                detection(self)

        # check if anti vm is enabled
        if self.anti_vm == True:
            from vmCheck import vmChecks_main
            # run anti vm checks and return results
            if vmChecks_main(self):
                # vm detected
                detection(self)



class procprotect:
    # get config
    def __init__(self, loop_timeout, debug, detectionReaction,
                 anti_debug, anti_debug_checks, anti_debug_custom_lists,
                 anti_vm, anti_vm_checks, anti_vm_custom_lists,
                ):
        # global
        self.loop_timeout = loop_timeout
        self.debug = debug
        self.detectionReaction = detectionReaction
        # anti debug
        self.anti_debug = anti_debug
        self.anti_debug_checks = anti_debug_checks
        self.anti_debug_custom_lists = anti_debug_custom_lists
        # anti vm
        self.anti_vm = anti_vm
        self.anti_vm_checks = anti_vm_checks
        self.anti_vm_custom_lists = anti_vm_custom_lists

    def run(self):
        import threading
        threading.Thread(
            target=checks(self)
        ).start()
                


"""
    # Create an instance of the procprotect class
    proc_protector = procprotect(
        # global (time in seconds)
        loop_timeout = 0.5,
        debug = True,
        detectionReaction = ["exit"],
        # anti debug
        anti_debug = True,
        anti_debug_checks =
        [
            "TracerPid",
            "WindowNames",
            "ProcessNames"
        ],
        anti_debug_custom_lists = {
            "windowNames": None,
            "ProcessNames": None,
        },
        # anti vm check
        anti_vm = True,
        anti_vm_checks =
        [
            "KnownIps",
            "VMPaths",
            "ProcessNames",
            "ManufactureRelease",
        ],
        anti_vm_custom_lists = {
            "knownIps": None,
            "ProcessNames": None,
        }
    )

    # Call the run() method on the proc_protector instance
    proc_protector.run()
"""