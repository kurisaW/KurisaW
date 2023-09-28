# RT-Thread v5.0.2 Released

Change Log Since v5.0.1 Release

## Kernel

* **include/rtdef.h:** Fixed two issues with atomic volatile in bsp/simulator compiled in VS2019; Added RT_USING_LIBC_ISO_ONLY macro; Supported POSIX-compatible errno.
* **src/kservice:** Improved rt_strerror function compatibility.
* Supported DM device id management; Supported multiple threads receiving the same event at the same time.
* No longer used RT_DEBUG_LOG in rtdebug.h.
* Tidied up debug macros and added RT DEBUGING CONTEXT.
* Fixed User mode MQ receive blocking issue.
* Added priority to message queues supported in POSIX interfaces.
* Removed recursion in mutex.
* Removed RT_DEBUG_xxx macros.
* Implemented default weak function for rt_hw_cpu_shutdown.

## Components

* **drivers**
  * **sensor:** Fixed an error in Sensor-V1 where the return type was inconsistent; Re-implemented sensor framework as Sensor-V2.
  * **fdt:** Added the device tree child node search macro.
  * **tty:** Fixed a bug on foreground app switch; Supported TCGETA/TCSETAF/TCSETAW/TCSETA commands.
  * **serial:** Fixed an issue where the serial port sometimes sent carriage returns repeatedly.
  * Supported the Core API for dd2.0.
  * **i2c:** Optimized control interface format to add available commands.
  * **rtc:** Reconfigurable clock framework; Fixed the bug that triggered the alarm for a single time and repeatedly used the timer that did not start.
  * **hwtimer:** Overflow is invalid in oneshot mode.
  * **core:** Revised the macros of header files.
  * **wlan:** Fixed some variables not used warnings when building.
  * Moved the core header files to the path: include/drivers/core.
* **lwp**
  * Executed elf with added executable permissions check.
  * Supported more features of signals from IEEE Std 1003.1-2017.
  * Fixed possible memory leak; Fixed the setup of fake LWP in sys_execve; Fixed socket addr bug; Fixed waitpid function exception.
  * Fixed bugs on LWP kill; Fixed exit(2) and added exit_group(2); Fixed rt_memcpy to lwp_memcpy in smart source; Fixed cmd_kill (Fix cmd_kill).
  * Added fops for dfs_v2 and fixed warning for eventfd_write and eventfd_read after dfs_v1 changes.
  * Cumulative updates of lwip and lwp.
* **libc**
  * Updated the allocation mode of the libc timer id.
  * Added signalfd for system call, Added eventfd for system call.
  * Implemented lightweight timezone configuration.
  * Renamed libc.c as posix/stdio.c.
  * Optimized the epoll code to remove restrictions on descriptors.
  * Adapted rt_channel, increased the generality of some rt_channel functionality on dfs v2, and standardized signalfd.
* **dfs**
  * Fixed variable usage errors in dfs elm.c.
  * Connected the posix mqueue pair to the file system fd.
  * Modified some function prototypes of the dfs_file_ops structure and function declarations.
  * Fixed fcntl(F_SETFL) bug, and modified the error code when opening a file failed.
  * Cumulative repair of dfs changes, including forced uninstallation and pread/pwrite changes.
  * dfs v2: Added cromfs function.
* **utilities**
  * Supported ulog_async_output_enabled, Supported adt API for DM.
  * Removed zmodem.
* **mm**
  * Improved output of list_page.
  * Added unmap page API.
* **net**
  * **sal/socket:** Fixed a BUG where calling closesocket interface triggered assertions when RT_DEBUG is enabled; Fixed duplicate free on allocated buffer.
  * **sal:** Fixed the IPv4 & v6 compiling issue.
* **ktime**
  * Added RT_USING_KTIME to Kconfig build.
  * Fixed some bugs with ktime.
  * Optimized the performance of high-precision timer, deleted a useless function.
* **sdio**
  * Enabled the eMMC internal cache to speed up transmission.
* **finsh**
  * Added msh autocomplete suboption feature.

## Drivers Device

* Prepared for device driver v2.0.

## Libcpu

* **aarch64:** Fixed default core binding failure on GICv2; Fixed aarch64 SMP startup failure; Supported hardware atomic; Fixed up FPU storage's size in stack and appended Q16 ~ Q31; Fixed HW atomic_t ops type from dword to qword; Supported public linker scripts; Changed aarch64 trap backtrace & coredump priority rating; Fixed an issue where AARCH64 Qemu failed to compile when SMP was disabled.
* **arm:** Fixed IAR compilation warnings: function "__LDREX" declared implicitly; Modified start_gcc.S; Fixed race condition with ldrex, strex; Fixed header file circular reference issue.
* **arc:** Fixed the thread switching bug in the arc architecture.
* **sim:** Fixed an issue with inconsistent function definitions.
* Added ARCH_ARM_CORTEX_M23 macro definitions.

## Tools

* Fixed .uvoptx/uvopt project name.
* Supported Env for finsh shell.
* Removed --dist-strip command.
* Corrected prompt message.

## Action

* Added CI to compile more drivers for the changed BSP, Added pkgs-test; Added the manual trigger and fail BSP check; Added more config for manual trigger.
* Added manual triggers for all STM32, Added the exp_STM32 SCons.
* Added the repo check for self-use; Added the code_owner review request; Added paths-ignore for format and static check.
* Fixed the path the YAML can't be folded; Fixed the flag of dist.
* Used env install script.

## Documents

* Added RT-Thread Code of Conduct; Added ktime readme doc; Added env vscode document.
* Fixed a typo in documentation.
* Updated env document, Updated qemu for windows doc; Updated quick_start_qemu_windows.

## Utest

* Adding volatile solves the problem that the test fails when the optimization level is high.
* Changed the thread size of the thread_tc thread stack to avoid stack anomalies caused by 64-bit machines; Changed the size of the thread stack to avoid stack anomalies.
* Added the signal dependency in signal test.

## BSP

* Added some new BSPs
  * ST: imx6ull, stm32u585-iot02a, stm32f405zgtx, stm32h563-st-nucleo, stm32h563-st-nucleo, stm32f407-rt-spark
  * SOPHGO: cv1800b
  * TI: msp432e401y-LaunchPad
* Supported Open Firmware API and model of PIC.
* Fixed MM32 compilation issues.
* stm32
  * stm32/stm32u5: Fixed GPIO interrupt error.
  * stm32/stm32l476-nucleo: Supported timer7 for RTduino; Supported PWM switch to SPI.
  * stm32/stm32wl55-st-nucleo: Fixed SCons compilation failure, improved link file, removed hardware floating-point support.
  * stm32/stm32f407-rt-spark: Release of the first version of rt

-spark BSP; Added rt-spark to run utest link snippets under GCC.
  * stm32/stm32f401nucleo/rtduino: Supported function switching of docking pins.
  * stm32/stm32l431-BearPi: Supported the MPU6050 module.
  * stm32/rtduino: Supported tone timers and limited the maximum number of pins checked; Supported function switching of docking pins; Fixed a demo bug and modified the SPI switch function.
  * stm32/i2c driver: Replaced stm32_udelay with rt_hw_us_delay.
  * stm32/build path: Example Modified the STM32 project generation path.
* qemu
  * qemu-virt64-aarch64: Fixed qemu failed to mount elm file system.
* airm2m
  * airm2m/air32f103: Synchronized lib changes, including SRAM locking, fixing RTC acquisition frequency errors; Updated the pin num command.
* wch
  * wch/riscv/ch32v307v: Added _head_end for link file.
  * wch/riscv/ch32v208w: Fixed C++ compiling errors.
  * wch/risc-v/Libraries/ch32_drivers: Fixed UART IRQ declaration.
* imxrt
  * imxrt/imxrt1060-nxp-evk: Solved the adaptation problem of RW007 module in MIMXRT1062-EVKB board; Imxrt1060 fix wrong image reference.
  * imxrt/imxrt1021-nxp-evk: Fixed RT_ASSERT undefined RT1021 FIXED.
* renesas
  * renesas/sdhi driver: Fixed an issue where SDHI could only read the first block when attempting multiple block reads.
  * Fixed part of renesas BSP and added related CI to it; Fixed an issue where Renesas BSP compilation would not pass.
  * Added hwtimer device for renesas.
* acm32
  * acm32/acm32f0x0-nucleo: Fixed scons --dist command error.
  * Fixed some issues with acm32 BSP and added CI to it.
* bouffalo_lab
  * bouffalo_lab/bl808/d0: Added bl808 d0 core SPI and I2C drivers.
* nuvoton
  * nuvoton/numaker-m467hj: Fixed related LVGL version issues.
* Infineon
  * Infineon/psoc6-evaluationkit-062S2: Added I2C config for psoc6-evaluationkit; Fixed i2c init error; Added cyw43012 wifi module; Added BT support.
* esp32_c3
  * Realized scons compilation of ESP32-C3.
* raspberry-pico:
  * Added software simulation SPI and software simulation I2C driver code.
  * Optimized Kconfig configuration.
* phytium
  * phytium/aarch32/e2000d_rtthread: Phytium e2000 update.
  * Fixed the Phytium QSPI driver.
* hpmicro
  * Three new BSPS are added: hpm6750evk2, hpm6300evk, and hpm6200evk.
* gd32
  * gd32/arm/gd32470z-lckfb: Add SDRAM driver.
* nuclei
  * nuclei/gd32vf103_rvstar: Add USB-related configuration headers.
