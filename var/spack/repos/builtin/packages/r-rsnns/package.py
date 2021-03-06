##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class RRsnns(Package):
    """The Stuttgart Neural Network Simulator (SNNS) is a library containing
    many standard implementations of neural networks. This package wraps the
    SNNS functionality to make it available from within R. Using the RSNNS
    low-level interface, all of the algorithmic functionality and flexibility
    of SNNS can be accessed. Furthermore, the package contains a convenient
    high-level interface, so that the most common neural network topologies
    and learning algorithms integrate seamlessly into R."""

    homepage = "http://sci2s.ugr.es/dicits/software/RSNNS"
    url      = "https://cran.r-project.org/src/contrib/RSNNS_0.4-7.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/RSNNS"

    version('0.4-7', 'ade7736611c456effb5f72e0ce0a1e6f')

    extends('r')

    depends_on('r-rcpp', type=nolink)

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)
