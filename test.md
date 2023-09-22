# RT-Thread v5.0.2 released

Change log since v5.0.1 released

## Kernel

* include/rtdef.h: Fixed two issues with atomic volatile in bsp/simulator compiled in vs2019 [(#7736)](https://github.com/RT-Thread/rt-thread/pull/7736)
* include/rtdef.h: Add RT_USING_LIBC_ISO_ONLY macro [(#8035)](https://github.com/RT-Thread/rt-thread/pull/8035)
* include/rtdef.h: Support POSIX compatible errno [(#7954)](https://github.com/RT-Thread/rt-thread/pull/7954)
* src/kservice: Improve rt_strerror function compatibility [(#8061)](https://github.com/RT-Thread/rt-thread/pull/8061)
* Support DM device id management
* Supports multiple threads receiving the same event at the same time [(#7786)](https://github.com/RT-Thread/rt-thread/pull/7786)
* Remove RT_DEBUG_xxx [(#7799)](https://github.com/RT-Thread/rt-thread/pull/7799)
* No longer use RT_DEBUG_LOG in rtdebug.h [(#7750)](https://github.com/RT-Thread/rt-thread/pull/7750)
* Tidy up debug macros and add RT DEBUGING CONTEXT [(#7805)](https://github.com/RT-Thread/rt-thread/pull/7805)
* Fix User mode mq receive cannot be blocked [(#7836)](https://github.com/RT-Thread/rt-thread/pull/7836)
* The priority of message queues supported in posix interfaces [(#7382)](https://github.com/RT-Thread/rt-thread/pull/7382)
* Except recursion in mutex [(#7856)](https://github.com/RT-Thread/rt-thread/pull/7856)
* Handle rt_hw_cpu_reset & rt_hw_cpu_shutdown [(#7928)](https://github.com/RT-Thread/rt-thread/pull/7928)

## Components

* drivers
  * sensor: Fixed a compilation error with inconsistent sensor V1 return types [(#7735)](https://github.com/RT-Thread/rt-thread/pull/7735)
  * fdt: Adds the device tree child node search macro [(#7377)](https://github.com/RT-Thread/rt-thread/pull/7377)
  * tty: Fixed bug on foreground app switch [(#7726)](https://github.com/RT-Thread/rt-thread/pull/7726)
  * tty: Supports TCGETA/TCSETAF/TCSETAW/TCSETA commands [(#7739)](https://github.com/RT-Thread/rt-thread/pull/7739)
  * serial: Fixed an issue where the serial port sometimes sends carriage returns repeatedly [(#7767)](https://github.com/RT-Thread/rt-thread/pull/7767)
  * Support the Core API for dd2.0 [(#7791)](https://github.com/RT-Thread/rt-thread/pull/7791)
  * i2c: Optimized controt interface format to add available commands [(#7806)](https://github.com/RT-Thread/rt-thread/pull/7806)
  * rtc: Reconfigurable clock framework [(#7794)](https://github.com/RT-Thread/rt-thread/pull/7794)
  * rtc: Fixed the bug that triggered the alarm for a single time and repeatedly used the timer that did not start [(#8019)](https://github.com/RT-Thread/rt-thread/pull/8019)
  * hwtimer: overflow is invalid in oneshot mode [(#7826)](https://github.com/RT-Thread/rt-thread/pull/7826)
  * Move the core header files to include/drivers/core [(#7869)](https://github.com/RT-Thread/rt-thread/pull/7869)
  * core: Revise the macros of header files [(#7884)](https://github.com/RT-Thread/rt-thread/pull/7884)
  * wlan: Fix some variables not used warnings when build [(#7925)](https://github.com/RT-Thread/rt-thread/pull/7925)
* lwp
  * clear ref to parent on waitpid() [(#7741)](https://github.com/RT-Thread/rt-thread/pull/7741)
  * execute elf add executable permissions check [(#7769)](https://github.com/RT-Thread/rt-thread/pull/7769/files)
  * support more feature of signal from IEEE Std 1003.1-2017 [(#7828)](https://github.com/RT-Thread/rt-thread/pull/7828)
  * Fix possible memory leak [(#7832)](https://github.com/RT-Thread/rt-thread/pull/7832)
  * Fix the setup of fake lwp in sys_execve [(#7855)](https://github.com/RT-Thread/rt-thread/pull/7855)
  * Fix socket addr bug [(#7876)](https://github.com/RT-Thread/rt-thread/pull/7876)
  * Add the system call epoll [(#7893)](https://github.com/RT-Thread/rt-thread/pull/7893)
  * Fix bugs on lwp kill [(#7892)](https://github.com/RT-Thread/rt-thread/pull/7892)
  * Cumulative updates of lwip and lwp [(#7888)](https://github.com/RT-Thread/rt-thread/pull/7888)
  * Add waitpid(-1) support [(#8020)](https://github.com/RT-Thread/rt-thread/pull/8020)
  * Fix exit(2) and add exit_group(2) [(#8005)](https://github.com/RT-Thread/rt-thread/pull/8005)
  * Fix rt_memcpy to lwp_memcpy in smart source [(#8033)](https://github.com/RT-Thread/rt-thread/pull/8033)
  * Fix of cmd_kill [(#8071)](https://github.com/RT-Thread/rt-thread/pull/8071/files)
* libc
  * Updated the allocation mode of the libc timer id [(#7744)](https://github.com/RT-Thread/rt-thread/pull/7744)
  * Add the system call eventfd [(#7835)](https://github.com/RT-Thread/rt-thread/pull/7835)
  * cleanup code [(#7839)](https://github.com/RT-Thread/rt-thread/pull/7839)
  * Add fops for dfs_v2 and rt_set_errno [(#7910)](https://github.com/RT-Thread/rt-thread/pull/7910)
  * Implement lightweith timezone configuration [(#7948)](https://github.com/RT-Thread/rt-thread/pull/7948)
  * Rename libc.c as posix/stdio.c [(#7930)](https://github.com/RT-Thread/rt-thread/pull/7930)
  * Optimize the epoll code to remove restrictions on descriptors [(#7951)](https://github.com/RT-Thread/rt-thread/pull/7951)
  * Add the system call signalfd [(#8001)](https://github.com/RT-Thread/rt-thread/pull/8001)
  * Adapt rt_channel, increase the generality of some rt_channel functionality on dfs v2, and standardize signalfd [(#8047)](https://github.com/RT-Thread/rt-thread/pull/8047)
* dfs
  * Fixed variable usage errors in dfs elm.c [(#7776)](https://github.com/RT-Thread/rt-thread/pull/7776)
  * Connect the posix mqueue pair to the file system fd [(#7768)](https://github.com/RT-Thread/rt-thread/pull/7768)
  * Modify some function prototypes of the dfs_file_ops structure and function declarations [(#7849)](https://github.com/RT-Thread/rt-thread/pull/7849)
  * Fix fcntl(F_SETFL) bug,and modify the error code when opening a file failed [(#7878)](https://github.com/RT-Thread/rt-thread/pull/7878)
  * Cumulative repair of dfs changes, including forced uninstallation and pread/pwrite changes [(#7887)](https://github.com/RT-Thread/rt-thread/pull/7887)
  * dfs v2: Add cromfs [(#7994)](https://github.com/RT-Thread/rt-thread/pull/7994)
* utilities
  * Support ulog_async_output_enabled [(#7775)](https://github.com/RT-Thread/rt-thread/pull/7775)
  * Support adt API for DM
  * Remove zmodem [(#7801)](https://github.com/RT-Thread/rt-thread/pull/7801)
* mm
  * Improve output of list_page [(#7779)](https://github.com/RT-Thread/rt-thread/pull/7779)
  * Add unmap page API [(#7834)](https://github.com/RT-Thread/rt-thread/pull/7834)
* net
  * sal/socket: Fixed a BUG where calling closesocket interface triggers assertions when RT_DEBUG is enabled [(#7793)](https://github.com/RT-Thread/rt-thread/pull/7793)
  * sal/socket: Fix duplicate free on allocated buffer [(#7818)](https://github.com/RT-Thread/rt-thread/pull/7818)
  * sal: Fix the IPv4&v6 compiling issue [(#7938)](https://github.com/RT-Thread/rt-thread/pull/7938)
* ktime
  * Add RT_USING_KTIME to kconfig build [(#7833)](https://github.com/RT-Thread/rt-thread/pull/7833)
  * Fix some bug with ktime
  * Optimize the performance of high precision timer, delete a useless function [(#7880)](https://github.com/RT-Thread/rt-thread/pull/7880)
* sdio
  * Enable the emmc internal cache to speed up transmission [(#7896)](https://github.com/RT-Thread/rt-thread/pull/7896)

## Drivers Device

* prepare for device driver v2.0 [(#7697)](https://github.com/RT-Thread/rt-thread/pull/7697)

## Libcpu

* aarch64: Failed to repair the gicv2 default kernel [(#7723)](https://github.com/RT-Thread/rt-thread/pull/7723)
* aarch64: Fix aarch64 smp startup failure [(#7760)](https://github.com/RT-Thread/rt-thread/pull/7760)
* aarch64: Support hardware atomic
* aarch64: Fixup fpu storage's size in stack and append Q16 ~ Q31 [(#7815)](https://github.com/RT-Thread/rt-thread/pull/7815)
* aarch64: Fixup HW atomic_t ops type from dword to qword [(#7861)](https://github.com/RT-Thread/rt-thread/pull/7861)
* aarch64: Support public linker scripts [(#7831)](https://github.com/RT-Thread/rt-thread/pull/7831)
* aarch64: Change aarch64 trap backtrace & coredump priority rating [(#8008)](https://github.com/RT-Thread/rt-thread/pull/8008)
* aarch64: Fixed an issue where AARCH64 Qemu failed to compile when SMP was disabled [(#8045)](https://github.com/RT-Thread/rt-thread/pull/8045)
* arm: Fixed IAR compilation warnings: function "__LDREX" declared implicitly [(#7733)](https://github.com/RT-Thread/rt-thread/pull/7733)
* arm: Modified start_gcc.S [(#7810)](https://github.com/RT-Thread/rt-thread/pull/7810)
* arm: fix race condition with ldrex,strex [(#7842)](https://github.com/RT-Thread/rt-thread/pull/7842)
* arc: Fixed the thread switching bug in arc architecture [(#7825)](https://github.com/RT-Thread/rt-thread/pull/7825)
* sim: Fixed an issue with inconsistent function definitions [(#7789)](https://github.com/RT-Thread/rt-thread/pull/7789)
* Add ARCH_ARM_CORTEX_M23 define [(#7895)](https://github.com/RT-Thread/rt-thread/pull/7895)

## Tools

* Fix .uvoptx/uvopt project name [(#7851)](https://github.com/RT-Thread/rt-thread/pull/7851)
* Support Env for fish shell [(#8026)](https://github.com/RT-Thread/rt-thread/pull/8026)
* Remove --dist-strip command [(#8037)](https://github.com/RT-Thread/rt-thread/pull/8037)

## Action

* Added CI to compile more drivers for the changed BSP [(#7738)](https://github.com/RT-Thread/rt-thread/pull/7738)
* Add manual triggers for all STM32 [(#7754)](https://github.com/RT-Thread/rt-thread/pull/7754)
* Add the exp_STM32 scons [(#7763)](https://github.com/RT-Thread/rt-thread/pull/7763)
* Add the repo check for self-use [(#7809)](https://github.com/RT-Thread/rt-thread/pull/7809)
* Add the code_owner review request [(#7829)](https://github.com/RT-Thread/rt-thread/pull/7829)
* Add paths-ignore for format and static check [(#7845)](https://github.com/RT-Thread/rt-thread/pull/7845)
* Add the manual trigger and fail bsp check [(#7919)](https://github.com/RT-Thread/rt-thread/pull/7919)
* Add more config for manual trigger [(#7970)](https://github.com/RT-Thread/rt-thread/pull/7970)
* Add pkgs-test [(#8053)](https://github.com/RT-Thread/rt-thread/pull/8053)
* Fix the path the yml can't in fold [(#7755)](https://github.com/RT-Thread/rt-thread/pull/7755)
* Fix the flag of dist [(#7770)](https://github.com/RT-Thread/rt-thread/pull/7770)
* Use env install script [(#8010)](https://github.com/RT-Thread/rt-thread/pull/8010)

## Documents

* add RT-Thread Code of Conduct [(#7728)](https://github.com/RT-Thread/rt-thread/pull/7728)
* Fix a typo in documentation [(#7773)](https://github.com/RT-Thread/rt-thread/pull/7773)
* Update env document [(#7844)](https://github.com/RT-Thread/rt-thread/pull/7844)
* Update quick_start_qemu_windows [(#7866)](https://github.com/RT-Thread/rt-thread/pull/7866)
* Update qemu for windows doc [(#7868)](https://github.com/RT-Thread/rt-thread/pull/7868)
* Add ktime readme doc [(#7870)](https://github.com/RT-Thread/rt-thread/pull/7870)
* Add env vscode document [(#7889)](https://github.com/RT-Thread/rt-thread/pull/7889)

## Utest

* Adding volatile solves the problem that the test fails when the optimization level is high [(#7717)](https://github.com/RT-Thread/rt-thread/pull/7717)
* Change the size of the thread_tc thread stack to avoid stack anomalies caused by 64-bit machines [(#8057)](https://github.com/RT-Thread/rt-thread/pull/8057)

## BSP

* Add some new BSPs
  * stm32/imx6ull : Add imx6ull smart board bsp [(#7716)](https://github.com/RT-Thread/rt-thread/pull/7716)
  * stm32/stm32u585-iot02a: Add B-U585I-IOT02A BSP [(#7778)](https://github.com/RT-Thread/rt-thread/pull/7778)
  * stm32/stm32f405zgtx: Add bsp support for stm32f405zgtx series [(#7971)](https://github.com/RT-Thread/rt-thread/pull/7971)
  * stm32/stm32h563-st-nucleo: Add NUCLEO-H563ZI bsp support [(#7987)](https://github.com/RT-Thread/rt-thread/pull/7987)
  * cv1800b: Added cv1800b bsp [(#7753)](https://github.com/RT-Thread/rt-thread/pull/7753)
* Support Open Firmware API and model of PIC [(#7788)](https://github.com/RT-Thread/rt-thread/pull/7788)
* Fix mm32 compilation issues [(#7780)](https://github.com/RT-Thread/rt-thread/pull/7780)
* stm32

  * stm32/stm32u5 : Fix gpio interrupt error [(#7720)](https://github.com/RT-Thread/rt-thread/pull/7720)
  * stm32/stm32l476-nucleo: Supports timer 7 for RTduino [(#7721)](https://github.com/RT-Thread/rt-thread/pull/7721)
  * stm32/stm32wl55-st-nucleo: Fixed scons compilation failure, improved link file, removed hardware floating-point support [(#7758)](https://github.com/RT-Thread/rt-thread/pull/7758)
  * stm32/stm32f407-rt-spark: Release of the first version of rt-spark bsp [(#7787)](https://github.com/RT-Thread/rt-thread/pull/7787)
  * stm32/stm32l476/rtduino: support PWM switch to SPI
  * stm32/stm32f401nucleo/rtduino: Supports function switching of docking pins [(#7901)](https://github.com/RT-Thread/rt-thread/pull/7901)
  * stm32/stm32l431-BearPi: BearPi supports the MPU6050 module [(#8059)](https://github.com/RT-Thread/rt-thread/pull/8059)
  * stm32/rtduino: Supports tone timers and limits the maximum number of pins checked [(#7792)](https://github.com/RT-Thread/rt-thread/pull/7792)
  * stm32/rtduino: Supports function switching of docking pins [(#7798)](https://github.com/RT-Thread/rt-thread/pull/7798)
  * stm32/rtduino: Fix a demo bug and modify the SPI switch function [(#7802)](https://github.com/RT-Thread/rt-thread/pull/7802)
  * stm32/i2c driver: Replace stm32_udelay as rt_hw_us_delay [(#7740)](https://github.com/RT-Thread/rt-thread/pull/7740)
  * stm32/build path: Example Modify the STM32 project generation path [(#7761)](https://github.com/RT-Thread/rt-thread/pull/7761)
* airm2m

  * airm2m/air32f103:  Synchronizes lib changes, including sram locking, fixing rtc acquisition frequency errors [(#7718)](https://github.com/RT-Thread/rt-thread/pull/7718)
  * airm2m/air32f103:  Update the pin num command [(#7390)](https://github.com/RT-Thread/rt-thread/pull/7390)
* wch

  * wch/riscv/ch32v307v: Add _head_end for link file [(#7729)](https://github.com/RT-Thread/rt-thread/pull/7729)
  * wch/riscv/ch32v208w: Fix C++ compling errors [(#7730)](https://github.com/RT-Thread/rt-thread/pull/7730)
  * wch/risc-v/Libraries/ch32_drivers: Fix UART IRQ declarion [(#7865)](https://github.com/RT-Thread/rt-thread/pull/7865)
* imxrt

  * imxrt/imxrt1060-nxp-evk: Solve the adaptation problem of RW007 module in MIMXRT1062-EVKB board [(#7734)](https://github.com/RT-Thread/rt-thread/pull/7734)
  * imxrt/imxrt1060-nxp-evk: Imxrt1060 fix wrong image reference [(#7743)](https://github.com/RT-Thread/rt-thread/pull/7743)
  * imxrt/imxrt1021-nxp-evk: Fix RT_ASSERT undefine RT1021 FIXED [(#7816)](https://github.com/RT-Thread/rt-thread/pull/7816)
* renesas
  * renesas/sdhi driver: Fixed an issue where SDHI could only read the first block when attempting multiple block reads [(#7737)](https://github.com/RT-Thread/rt-thread/pull/7737)
  * Fixed part of renesas bsp and added related ci to it [(#7782)](https://github.com/RT-Thread/rt-thread/pull/7782)
  * Fixed an issue where Renesas bsp compilation would not pass [(#7804)](https://github.com/RT-Thread/rt-thread/pull/7804)
  * Add hwtimer device for renesas [(#8006)](https://github.com/RT-Thread/rt-thread/pull/8006)
* acm32
  * acm32/acm32f0x0-nucleo: Fix scons --dist command error [(#7749)](https://github.com/RT-Thread/rt-thread/pull/7749)
  * Fixed some issues with acm32 bsp and added ci to it [(#7783)](https://github.com/RT-Thread/rt-thread/pull/7783)
* bouffalo_lab
  * bouffalo_lab/bl808/d0: Added bl808 d0 core spi and i2c drivers [(#7756)](https://github.com/RT-Thread/rt-thread/pull/7756)
* nuvoton
  * nuvoton/numaker-m467hj: Fix related LVGL version issues [(#7762)](https://github.com/RT-Thread/rt-thread/pull/7762)
* Infineon
  * Infineon/psoc6-evaluationkit-062S2: Add I2C4 config for psoc6-evaluationkit [(#7796)](https://github.com/RT-Thread/rt-thread/pull/7796)
  * Infineon/psoc6-evaluationkit-062S2: Fix i2c init error [(#7817)](https://github.com/RT-Thread/rt-thread/pull/7817)
  * Infineon/psoc6-evaluationkit-062S2: Add cyw43012 wifi module [(#7937)](https://github.com/RT-Thread/rt-thread/pull/7937)
  * Infineon/psoc6-evaluationkit-062S2: Add bt support [(#8028)](https://github.com/RT-Thread/rt-thread/pull/8028)
* msp432e401y-LaunchPad
  * add msp432e401y-LaunchPad BSP v0.1 [(#7823)](https://github.com/RT-Thread/rt-thread/pull/7823)

* esp32_c3
  * Realization of scons compilation of ESP32-C3 [(#7821)](https://github.com/RT-Thread/rt-thread/pull/7821)

* raspberry-pico:
  * Added software simulation spi and software simulation i2c driver code [(#7890)](https://github.com/RT-Thread/rt-thread/pull/7890)

* phytium
  * phytium/aarch32/e2000d_rtthread: Phytium e2000 update [(#7900)](https://github.com/RT-Thread/rt-thread/pull/7900)
  * Fixed the Phytium qspi driver [(#7914)](https://github.com/RT-Thread/rt-thread/pull/7914)

* hpmicro
  * Three new BSPS are added: hpm6750evk2, hpm6300evk, and hpm6200evk [(#7956)](https://github.com/RT-Thread/rt-thread/pull/7956)

* gd32
  * gd32/arm/gd32470z-lckfb: Add SDRAM driver [(#7965)](https://github.com/RT-Thread/rt-thread/pull/7965)

> 最新合并的PR：[#8071](https://github.com/RT-Thread/rt-thread/pull/8071)
