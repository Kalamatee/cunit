Summary: A unit testing framework for 'C'
Name: CUnit
Version : 1.0
Release: 7
Epoch: 1
Source: http://www.sourceforge.net/projects/cunit
Group: Development/Tools
Copyright: GPL
URL: http://cunit.sourceforge.net
Packager: Anil Kumar <aksaharan@yahoo.com>

%description
CUnit is unit testing framework for C.

%prep
echo "Preparing for Installation."

%build
echo "Preparing for Building."
cd $RPM_BUILD_ROOT && \
./configure --prefix=%{_prefix} && \
make

%install
echo "Preparing for Make install."
cd $RPM_BUILD_ROOT && \
make install

%clean

%files
%defattr(-,root,root)

########### Include Files
%{_prefix}/include/CUnit/Automated.h
%{_prefix}/include/CUnit/Console.h
%{_prefix}/include/CUnit/Curses.h
%{_prefix}/include/CUnit/CUnit.h
%{_prefix}/include/CUnit/Errno.h
%{_prefix}/include/CUnit/TestDB.h

########## Library File
%{_prefix}/lib/libcunit.a

########## Manpage Files
%{_prefix}/man/man3/add_test_case.3
%{_prefix}/man/man3/add_test_group.3
%{_prefix}/man/man3/ASSERT.3
%{_prefix}/man/man3/automated_run_tests.3
%{_prefix}/man/man3/cleanup_registry.3
%{_prefix}/man/man3/console_run_tests.3
%{_prefix}/man/man3/curses_run_tests.3
%{_prefix}/man/man3/get_error.3
%{_prefix}/man/man3/get_registry.3
%{_prefix}/man/man3/initialize_registry.3
%{_prefix}/man/man3/set_output_filename.3
%{_prefix}/man/man3/set_registry.3
%{_prefix}/man/man8/CUnit.8

########## Share information and Example Files 
%{_prefix}/share/CUnit-1.0-7/Example/Automated/README
%{_prefix}/share/CUnit-1.0-7/Example/Automated/AutomatedTest
%{_prefix}/share/CUnit-1.0-7/Example/Console/README
%{_prefix}/share/CUnit-1.0-7/Example/Console/ConsoleTest
%{_prefix}/share/CUnit-1.0-7/Example/Curses/README
%{_prefix}/share/CUnit-1.0-7/Example/Curses/CursesTest
%{_prefix}/share/CUnit/CUnit-List.dtd
%{_prefix}/share/CUnit/CUnit-List.xsl
%{_prefix}/share/CUnit/CUnit-Run.dtd
%{_prefix}/share/CUnit/CUnit-Run.xsl

# Add the change log in ChangeLog file located under source home directory.
# The same file is inturn used internally to populate the change log for the RPM
# creation.