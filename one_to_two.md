# RT-Thread v5.0.2 released

Change log since v5.0.1 released

## Kernel

* include/rtdef.h: Fixed two issues with atomic volatile in bsp/simulator compiled in vs2019; Add RT_USING_LIBC_ISO_ONLY macro; Support POSIX compatible errno
* src/kservice: Improve rt_strerror function compatibility
* Support DM device id management; Supports multiple threads receiving the same event at the same time
* No longer use RT_DEBUG_LOG in rtdebug.h
* Tidy up debug macros and add RT DEBUGING CONTEXT
* Fix User mode mq receive cannot be blocked
* The priority of message queues supported in posix interfaces
* Except recursion in mutex
* Handle rt_hw_cpu_reset & rt_hw_cpu_shutdown

## Components

* drivers
  * sensor: Fixed a compilation error with inconsistent sensor V1 return types
  * fdt: Adds the device tree child node search macro
  * tty: Fixed bug on foreground app switch; Supports TCGETA/TCSETAF/TCSETAW/TCSETA commands
  * serial: Fixed an issue where the serial port sometimes sends carriage returns repeatedly
  * Support the Core API for dd2.0
  * i2c: Optimized controt interface format to add available commands
  * rtc: Reconfigurable clock framework; Fixed the bug that triggered the alarm for a single time and repeatedly used the timer that did not start
  * hwtimer: overflow is invalid in oneshot mode
  * core: Revise the macros of header files
  * wlan: Fix some variables not used warnings when build
* lwp
  * clear ref to parent on waitpid()
  * execute elf add executable permissions check
  * support more feature of signal from IEEE Std 1003.1-2017
  * Fix possible memory leak; Fix the setup of fake lwp in sys_execve; Fix socket addr bug; 
  * Fix bugs on lwp kill; Fix exit(2) and add exit_group(2); Fix rt_memcpy to lwp_memcpy in smart source; Fix of cmd_kill
  * Add the system call epoll, waitpid(-1) support
  * Cumulative updates of lwip and lwp
* libc
  * Updated the allocation mode of the libc timer id
  * Add the system call eventfd signalfd; Add fops for dfs_v2 and rt_set_errno
  * Implement lightweith timezone configuration
  * Rename libc.c as posix/stdio.c
  * Optimize the epoll code to remove restrictions on descriptors
  * Adapt rt_channel, increase the generality of some rt_channel functionality on dfs v2, and standardize signalfd 
* dfs
  * Fixed variable usage errors in dfs elm.c
  * Connect the posix mqueue pair to the file system fd
  * Modify some function prototypes of the dfs_file_ops structure and function declarations
  * Fix fcntl(F_SETFL) bug,and modify the error code when opening a file failed
  * Cumulative repair of dfs changes, including forced uninstallation and pread/pwrite changes
  * dfs v2: Add cromfs function
* utilities
  * Support ulog_async_output_enabled, Support adt API for DM
  * Remove zmodem
* mm
  * Improve output of list_page
  * Add unmap page API
* net
  * sal/socket: Fixed a BUG where calling closesocket interface triggers assertions when RT_DEBUG is enabled; Fix duplicate free on allocated buffer
  * sal: Fix the IPv4&v6 compiling issue 
* ktime
  * Add RT_USING_KTIME to kconfig build 
  * Fix some bug with ktime
  * Optimize the performance of high precision timer, delete a useless function 
* sdio
  * Enable the emmc internal cache to speed up transmission 
* finsh
  * Added msh autocomplete suboption feature

## Drivers Device

* prepare for device driver v2.0 

## Libcpu

* aarch64: Failed to repair the gicv2 default kernel; Fix aarch64 smp startup failure; Support hardware atomic; Fixup fpu storage's size in stack and append Q16 ~ Q31; Fixup HW atomic_t ops type from dword to qword; Support public linker scripts; Change aarch64 trap backtrace & coredump priority rating; Fixed an issue where AARCH64 Qemu failed to compile when SMP was disabled.
* arm: Fixed IAR compilation warnings: function "__LDREX" declared implicitly; Modified start_gcc.S; Fix race condition with ldrex,strex; Fixed header file circular reference issue.
* arc: Fixed the thread switching bug in arc architecture 
* sim: Fixed an issue with inconsistent function definitions 
* Add ARCH_ARM_CORTEX_M23 define 

## Tools

* Fix .uvoptx/uvopt project name 
* Support Env for fish shell 
* Remove --dist-strip command 
* Correct prompt message

## Action

* Add CI to compile more drivers for the changed BSP, Add pkgs-test; Add the manual trigger and fail bsp check; Add more config for manual trigger 
* Add manual triggers for all STM32, Add the exp_STM32 scons
* Add the repo check for self-use; Add the code_owner review request; Add paths-ignore for format and static check
* Fix the path the yml can't in fold; Fix the flag of dist 
* Use env install script 

## Documents

* Add RT-Thread Code of Conduct; Add ktime readme doc; Add env vscode document 
* Fix a typo in documentation 
* Update env document, Update qemu for windows doc; Update quick_start_qemu_windows

## Utest

* Adding volatile solves the problem that the test fails when the optimization level is high 
* Change the size of the thread_tc thread stack to avoid stack anomalies caused by 64-bit machines; Change the size of the thread stack to avoid stack anomalies
* Add the signal dependency in signal test 

## BSP

* Add some new BSPs
  * ST: imx6ull, stm32u585-iot02a, stm32f405zgtx, stm32h563-st-nucleo, stm32h563-st-nucleo, stm32f407-rt-spark
  * SOPHGO: cv1800b
  * TI: msp432e401y-LaunchPad
* Support Open Firmware API and model of PIC 
* Fix mm32 compilation issues 
* stm32

  * stm32/stm32u5 : Fix gpio interrupt error 
  * stm32/stm32l476-nucleo: Supports timer 7 for RTduino; support PWM switch to SPI
  * stm32/stm32wl55-st-nucleo: Fixed scons compilation failure, improved link file, removed hardware floating-point support 
  * stm32/stm32f407-rt-spark: Release of the first version of rt-spark bsp; Add rt-spark to run utest link snippets under gcc
  * stm32/stm32f401nucleo/rtduino: Supports function switching of docking pins 
  * stm32/stm32l431-BearPi: BearPi supports the MPU6050 module 
  * stm32/rtduino: Supports tone timers and limits the maximum number of pins checked; Supports function switching of docking pins; Fix a demo bug and modify the SPI switch function 
  * stm32/i2c driver: Replace stm32_udelay as rt_hw_us_delay 
  * stm32/build path: Example Modify the STM32 project generation path 
* qemu
  * qemu-virt64-aarch64: Fix qemu failed to mount elm file system
* airm2m
  * airm2m/air32f103:  Synchronizes lib changes, including sram locking, fixing rtc acquisition frequency errors; Update the pin num command 
* wch

  * wch/riscv/ch32v307v: Add _head_end for link file 
  * wch/riscv/ch32v208w: Fix C++ compling errors 
  * wch/risc-v/Libraries/ch32_drivers: Fix UART IRQ declarion 
* imxrt

  * imxrt/imxrt1060-nxp-evk: Solve the adaptation problem of RW007 module in MIMXRT1062-EVKB board; Imxrt1060 fix wrong image reference 
  * imxrt/imxrt1021-nxp-evk: Fix RT_ASSERT undefine RT1021 FIXED 
* renesas
  * renesas/sdhi driver: Fixed an issue where SDHI could only read the first block when attempting multiple block reads 
  * Fixed part of renesas bsp and added related ci to it; Fixed an issue where Renesas bsp compilation would not pass 
  * Add hwtimer device for renesas 
* acm32
  * acm32/acm32f0x0-nucleo: Fix scons --dist command error 
  * Fixed some issues with acm32 bsp and added ci to it 
* bouffalo_lab
  * bouffalo_lab/bl808/d0: Added bl808 d0 core spi and i2c drivers 
* nuvoton
  * nuvoton/numaker-m467hj: Fix related LVGL version issues 
* Infineon
  * Infineon/psoc6-evaluationkit-062S2: Add I2C config for psoc6-evaluationkit; Fix i2c init error; Add cyw43012 wifi module; Add bt support 
* esp32_c3
  * Realization of scons compilation of ESP32-C3 
* raspberry-pico:
  * Added software simulation spi and software simulation i2c driver code 
  * Optimize Kconfig configuration
* phytium
  * phytium/aarch32/e2000d_rtthread: Phytium e2000 update 
  * Fixed the Phytium qspi driver 
* hpmicro
  * Three new BSPS are added: hpm6750evk2, hpm6300evk, and hpm6200evk 
* gd32
  * gd32/arm/gd32470z-lckfb: Add SDRAM driver 
* nuclei
  * nuclei/gd32vf103_rvstar: Add USB-related configuration headers

> 最新合并的PR：[#8095](https://github.com/RT-Thread/rt-thread/pull/8095)
